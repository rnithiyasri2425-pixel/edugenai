from transformers import pipeline

try:
    explanation_pipeline = pipeline(
        "text2text-generation",
        model="MBZUAI/LaMini-Flan-T5-783M"
    )
    model_error = None
except Exception as e:
    explanation_pipeline = None
    model_error = str(e)

def explain_concept(concept: str) -> str:
    if explanation_pipeline is None:
        return "The local explanation model could not be loaded.\n\nModel error: " + model_error
    prompt = f"""
Explain the following concept to a student in simple language.
Concept:
{concept}
Requirements:
- Give a simple definition.
- Explain the concept step by step.
- Give a simple example.
- Avoid unnecessarily complicated words.
"""
    try:
        result = explanation_pipeline(prompt, max_new_tokens=300, do_sample=True, temperature=0.7)
        return result[0]["generated_text"] if result else "Sorry, I could not explain the concept."
    except Exception as e:
        return f"Error while explaining concept: {str(e)}"
