import streamlit as st
import re
import random
from typing import List, Dict, Tuple
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

def setup_nltk():
    """Setup NLTK data with fallback for different versions."""
    resources_to_download = ['stopwords']
    
    # Handle punkt/punkt_tab compatibility
    punkt_resources = ['punkt_tab', 'punkt']
    
    for resource in punkt_resources:
        try:
            if resource == 'punkt_tab':
                nltk.data.find('tokenizers/punkt_tab')
            else:
                nltk.data.find('tokenizers/punkt')
            break
        except LookupError:
            try:
                nltk.download(resource, quiet=True)
                break
            except:
                continue
    
    # Download stopwords
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)

# Setup NLTK data
setup_nltk()

class ContentGenerator:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        
    def extract_key_concepts(self, text: str, num_concepts: int = 10) -> List[str]:
        """Extract key concepts from the text using word frequency analysis."""
        # Tokenize and clean text
        words = word_tokenize(text.lower())
        words = [word for word in words if word.isalpha() and word not in self.stop_words]
        
        # Get most common words
        word_freq = Counter(words)
        key_concepts = [word[0] for word in word_freq.most_common(num_concepts)]
        
        return key_concepts
    
    def extract_sentences(self, text: str) -> List[str]:
        """Extract sentences from the text."""
        sentences = sent_tokenize(text)
        return [sentence.strip() for sentence in sentences if len(sentence.strip()) > 20]
    
    def generate_assignments(self, text: str, topic: str = "") -> List[str]:
        """Generate 2 assignment questions based on the content."""
        key_concepts = self.extract_key_concepts(text, 5)
        sentences = self.extract_sentences(text)
        
        assignments = []
        
        # Assignment templates
        assignment_templates = [
            f"Write a comprehensive essay analyzing the relationship between {key_concepts[0] if key_concepts else 'the main concept'} and {key_concepts[1] if len(key_concepts) > 1 else 'related themes'} discussed in the provided material. Support your analysis with specific examples.",
            
            f"Critically evaluate the importance of {key_concepts[0] if key_concepts else 'the central theme'} in the context of {topic if topic else 'the subject matter'}. Discuss potential implications and provide your reasoned opinion.",
            
            f"Compare and contrast different perspectives on {key_concepts[0] if key_concepts else 'the main topic'} presented in the material. What are the strengths and weaknesses of each viewpoint?",
            
            f"Design a practical application or solution that addresses the concepts of {key_concepts[0] if key_concepts else 'the main idea'} and {key_concepts[2] if len(key_concepts) > 2 else 'related principles'}. Explain your reasoning and expected outcomes.",
            
            f"Analyze the cause-and-effect relationships involving {key_concepts[0] if key_concepts else 'key elements'} discussed in the text. How do these relationships impact {topic if topic else 'the overall understanding'}?"
        ]
        
        # Select 2 random assignments
        selected_assignments = random.sample(assignment_templates, min(2, len(assignment_templates)))
        assignments.extend(selected_assignments)
        
        return assignments
    
    def generate_quiz_questions(self, text: str) -> List[Dict]:
        """Generate 3 multiple-choice quiz questions based on the content."""
        sentences = self.extract_sentences(text)
        key_concepts = self.extract_key_concepts(text, 15)
        
        quiz_questions = []
        used_concepts = set()
        
        # Question generation strategies
        for i in range(3):
            if i < len(sentences) and key_concepts:
                # Strategy 1: Fill-in-the-blank style
                sentence = sentences[i]
                available_concepts = [concept for concept in key_concepts if concept not in used_concepts]
                
                if available_concepts and len(sentence.split()) > 8:
                    concept = available_concepts[0]
                    used_concepts.add(concept)
                    
                    # Try to find the concept in the sentence
                    if concept in sentence.lower():
                        question_text = sentence.replace(concept, "______", 1)
                        question = f"Complete the following statement: {question_text}"
                    else:
                        question = f"According to the text, what is most closely associated with {concept}?"
                    
                    # Generate options
                    correct_answer = concept.title()
                    wrong_options = [c.title() for c in available_concepts[1:4] if c != concept]
                    
                    # Add some generic wrong options if not enough
                    generic_options = ["Economic factors", "Social dynamics", "Environmental concerns", "Technological advancement", "Cultural influence"]
                    while len(wrong_options) < 3:
                        generic_option = random.choice([opt for opt in generic_options if opt not in wrong_options])
                        wrong_options.append(generic_option)
                    
                    options = [correct_answer] + wrong_options[:3]
                    random.shuffle(options)
                    
                    quiz_questions.append({
                        "question": question,
                        "options": options,
                        "correct_answer": correct_answer
                    })
        
        # If we don't have enough questions, generate some generic ones
        while len(quiz_questions) < 3:
            remaining_concepts = [c for c in key_concepts if c not in used_concepts]
            if remaining_concepts:
                concept = remaining_concepts[0]
                used_concepts.add(concept)
                
                generic_questions = [
                    f"What role does {concept} play in the discussed topic?",
                    f"Which of the following best describes {concept}?",
                    f"According to the material, {concept} is most important because:"
                ]
                
                question = random.choice(generic_questions)
                correct_answer = f"It is a central concept in the material"
                wrong_options = [
                    "It is mentioned only briefly",
                    "It contradicts the main argument",
                    "It is an outdated concept"
                ]
                
                options = [correct_answer] + wrong_options
                random.shuffle(options)
                
                quiz_questions.append({
                    "question": question,
                    "options": options,
                    "correct_answer": correct_answer
                })
            else:
                break
        
        return quiz_questions

def main():
    st.set_page_config(
        page_title="Educational Content Generator",
        page_icon="📚",
        layout="wide"
    )
    
    st.title("📚 Educational Content Generator")
    st.markdown("Generate assignments and quiz questions from any document or topic!")
    
    # Initialize the generator
    generator = ContentGenerator()
    
    # Sidebar for input options
    st.sidebar.header("Input Options")
    input_method = st.sidebar.radio(
        "Choose input method:",
        ["Text Input", "File Upload"]
    )
    
    text_content = ""
    topic = ""
    
    if input_method == "Text Input":
        topic = st.sidebar.text_input("Topic/Subject (optional):", placeholder="e.g., Climate Change, Machine Learning")
        text_content = st.text_area(
            "Enter your document or topic content:",
            height=300,
            placeholder="Paste your document content here..."
        )
    
    elif input_method == "File Upload":
        topic = st.sidebar.text_input("Topic/Subject (optional):", placeholder="e.g., Climate Change, Machine Learning")
        uploaded_file = st.file_uploader("Upload a text file", type=['txt'])
        if uploaded_file is not None:
            text_content = str(uploaded_file.read(), "utf-8")
            st.text_area("File Content Preview:", value=text_content[:500] + "..." if len(text_content) > 500 else text_content, height=150)
    
    # Generate content button
    if st.button("🎯 Generate Educational Content", type="primary"):
        if text_content.strip():
            with st.spinner("Generating assignments and quiz questions..."):
                try:
                    # Generate assignments
                    assignments = generator.generate_assignments(text_content, topic)
                    
                    # Generate quiz questions
                    quiz_questions = generator.generate_quiz_questions(text_content)
                    
                    # Display results
                    col1, col2 = st.columns([1, 1])
                    
                    with col1:
                        st.header("📝 Assignment Questions")
                        for i, assignment in enumerate(assignments, 1):
                            with st.expander(f"Assignment {i}", expanded=True):
                                st.write(assignment)
                    
                    with col2:
                        st.header("❓ Quiz Questions")
                        for i, question in enumerate(quiz_questions, 1):
                            with st.expander(f"Question {i}", expanded=True):
                                st.write(f"**{question['question']}**")
                                st.write("Options:")
                                for j, option in enumerate(question['options'], 1):
                                    marker = "✅" if option == question['correct_answer'] else "•"
                                    st.write(f"{marker} {j}. {option}")
                                st.write(f"**Correct Answer:** {question['correct_answer']}")
                    
                    # Download section
                    st.header("💾 Download Results")
                    
                    # Prepare download content
                    download_content = f"Educational Content Generated from: {topic if topic else 'Provided Document'}\n\n"
                    download_content += "ASSIGNMENT QUESTIONS:\n"
                    download_content += "=" * 50 + "\n\n"
                    
                    for i, assignment in enumerate(assignments, 1):
                        download_content += f"Assignment {i}:\n{assignment}\n\n"
                    
                    download_content += "QUIZ QUESTIONS:\n"
                    download_content += "=" * 50 + "\n\n"
                    
                    for i, question in enumerate(quiz_questions, 1):
                        download_content += f"Question {i}: {question['question']}\n"
                        for j, option in enumerate(question['options'], 1):
                            download_content += f"  {j}. {option}\n"
                        download_content += f"Correct Answer: {question['correct_answer']}\n\n"
                    
                    st.download_button(
                        label="📥 Download as Text File",
                        data=download_content,
                        file_name=f"educational_content_{topic.replace(' ', '_').lower() if topic else 'generated'}.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    st.info("Please ensure you have valid text content and try again.")
        
        else:
            st.warning("Please provide some text content to generate educational materials.")
    
    # Instructions and tips
    with st.expander("ℹ️ How to Use This Tool"):
        st.markdown("""
        ### Instructions:
        1. **Choose Input Method**: Select either text input or file upload
        2. **Provide Content**: Enter or upload your document content
        3. **Add Topic** (Optional): Specify the subject for better context
        4. **Generate**: Click the button to create assignments and quizzes
        
        ### Tips for Better Results:
        - Provide substantial content (at least a few paragraphs)
        - Use clear, well-structured text
        - Include key concepts and important information
        - Specify the topic/subject for more relevant questions
        
        ### Features:
        - **2 Assignment Questions**: Essay prompts and analytical questions
        - **3 Quiz Questions**: Multiple-choice questions with answers
        - **Smart Analysis**: Uses NLP to identify key concepts
        - **Download Option**: Save generated content as a text file
        """)

if __name__ == "__main__":
    main()
