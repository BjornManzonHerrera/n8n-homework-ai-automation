# Essential imports for essay generation system
import gradio as gr
from transformers import pipeline
import re, json
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.INFO)

def extract_json_from_text(text):
    """Extract JSON from text using multiple strategies"""
    # Strategy 1: Find JSON block after the original prompt
    prompt_end = text.find('JSON Response:')
    if prompt_end != -1:
        json_part = text[prompt_end + len('JSON Response:'):].strip()
    else:
        json_part = text
    
    # Strategy 2: Find first complete JSON object
    json_matches = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', json_part)
    for match in json_matches:
        try:
            parsed = json.loads(match)
            if isinstance(parsed, dict) and 'header' in parsed and 'body' in parsed:
                return match
        except json.JSONDecodeError:
            continue
    
    # Strategy 3: Look for JSON-like structure and attempt to fix common issues
    match = re.search(r'\{[\s\S]*?\}', json_part)
    if match:
        json_candidate = match.group(0)
        # Try to fix common issues
        json_candidate = re.sub(r'(?<!\\)"([^"]*?)(?<!\\)"', r'"\1"', json_candidate)
        return json_candidate
    
    return None

def extract_json_from_flan_output(text):
    """Extract JSON from FLAN-T5 output with specific handling"""
    # FLAN-T5 might output JSON directly or with minimal formatting
    text = text.strip()
    
    # Look for JSON-like structure
    json_match = re.search(r'\{[\s\S]*\}', text)
    if json_match:
        json_candidate = json_match.group(0)
        
        # Clean up common FLAN-T5 formatting issues
        json_candidate = re.sub(r'(?<!\\)\\n', '\\n', json_candidate)  # Fix newlines
        json_candidate = re.sub(r'(?<!\\)\\t', '\\t', json_candidate)  # Fix tabs
        
        return json_candidate
    
    # If no JSON found, try to create structure from the raw text
    if len(text) > 20:  # Reasonable content length
        # Try to extract meaningful content
        return f'{{"header": "Student Name | Subject | Module | Essay", "body": "{text}"}}'
    
    return None

# 🚀 Use FLAN-T5-large for better instruction following and essay generation
# FLAN-T5 is specifically trained for instruction following tasks
print("Loading FLAN-T5-large model...")
generator = pipeline("text2text-generation", model="google/flan-t5-large", 
                    device_map="auto", torch_dtype="auto")
print("Model loaded successfully!")

def generate_essay(assignment_name: str, assignment_description: str) -> str:
    """
    Generate a structured academic essay using FLAN-T5-large
    
    Args:
        assignment_name: The name/title of the assignment
        assignment_description: Detailed description of what the essay should cover
        
    Returns:
        JSON string containing header and body fields
    """
    # 🧠 FLAN-T5 optimized prompt for structured essay generation
    # This prompt is specifically designed to work with instruction-following models
    prompt = f"""Write a complete 500-word academic essay about: {assignment_name}

Instructions: {assignment_description}

Structure your essay with:
1. Introduction paragraph
2. Main body paragraphs with evidence and analysis
3. Conclusion paragraph

Write a comprehensive, well-structured essay that addresses all the requirements."""

    try:
        logging.info(f"Generating essay for: {assignment_name}")
        
        # 🔄 Generate with FLAN-T5 optimized parameters
        # These parameters are tuned for coherent, diverse text generation
        generated = generator(
            prompt,
            max_length=800,      # Increased for longer essays
            do_sample=True,      # Enable sampling for more creative output
            temperature=0.7,     # Balanced creativity vs coherence
            top_p=0.9,          # Nucleus sampling for quality
            repetition_penalty=1.2,  # Reduce repetition
            num_return_sequences=1
        )

        if not generated or len(generated) == 0:
            raise ValueError("No output generated from model")

        # Extract the generated text
        result = generated[0]["generated_text"]
        logging.info(f"Generated text length: {len(result)} characters")
        
        # Clean up the generated text
        essay_content = result.strip()
        
        # Ensure we have substantial content
        if len(essay_content) < 100:
            # Generate fallback content if output is too short
            essay_content = f"""Introduction:
This essay examines {assignment_name} as outlined in the assignment requirements. {assignment_description}

Main Analysis:
The topic requires careful consideration of multiple perspectives and evidence-based arguments. Through systematic examination of the key concepts, we can develop a comprehensive understanding of the subject matter. The analysis reveals important insights that contribute to our overall understanding of the topic.

Critical Evaluation:
Further examination of the evidence demonstrates the complexity of the issues involved. The various factors must be weighed carefully to reach meaningful conclusions. This analysis provides a foundation for understanding the broader implications of the topic.

Conclusion:
In conclusion, this examination of {assignment_name} reveals the importance of thorough analysis and critical thinking. The insights gained from this study contribute to a deeper understanding of the subject matter and its broader implications."""

        # 📋 Return structured JSON response
        response = {
            "header": "Student Name | Subject | Module | Essay",
            "body": essay_content
        }
        
        return json.dumps(response, indent=2)

    except Exception as e:
        logging.error(f"Error generating essay: {str(e)}")
        # 🔄 Fallback response for any errors
        fallback_response = {
            "header": "Student Name | Subject | Module | Essay",
            "body": f"Essay Analysis: {assignment_name}\n\n{assignment_description}\n\nThis assignment requires comprehensive analysis and structured argumentation. The key concepts involve understanding the requirements and developing a coherent response that demonstrates mastery of the subject matter."
        }
        return json.dumps(fallback_response, indent=2)

# 🎨 Create Gradio interface for easy web access
def create_gradio_interface():
    """Create and configure the Gradio interface"""
    
    def process_essay_request(name, description):
        """Process essay generation request from Gradio interface"""
        if not name or not description:
            return json.dumps({
                "header": "Student Name | Subject | Module | Essay",
                "body": "Please provide both assignment name and description."
            }, indent=2)
        
        return generate_essay(name, description)
    
    # 🎯 Create Gradio interface with custom styling
    interface = gr.Interface(
        fn=process_essay_request,
        inputs=[
            gr.Textbox(
                label="Assignment Name",
                placeholder="e.g., Climate Change Impact Essay",
                lines=1
            ),
            gr.Textbox(
                label="Assignment Description", 
                placeholder="e.g., Write a 500-word essay analyzing the impact of climate change on global ecosystems...",
                lines=3
            )
        ],
        outputs=gr.Code(
            label="Generated Essay (JSON)",
            language="json"
        ),
        title="🎓 Academic Essay Generator",
        description="Generate structured academic essays using AI. Powered by FLAN-T5-large for high-quality, instruction-following text generation.",
        examples=[
            ["Climate Change Essay", "Write a 500-word essay about the impact of climate change on global ecosystems"],
            ["Technology in Education", "Analyze how technology has transformed modern education and learning methods"],
            ["Social Media Impact", "Examine the effects of social media on interpersonal communication and society"]
        ],
        theme=gr.themes.Soft(),
        allow_flagging="never"
    )
    
    return interface

# 🚀 Launch the Gradio interface
if __name__ == "__main__":
    print("Starting Academic Essay Generator...")
    interface = create_gradio_interface()
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )