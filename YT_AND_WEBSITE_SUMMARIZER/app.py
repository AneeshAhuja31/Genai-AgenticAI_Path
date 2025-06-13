import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader
from langchain_community.document_loaders.youtube import TranscriptFormat



st.title("Summarize Text from YT or Website")
st.subheader("Summarize URL")


with st.sidebar:
    groq_api_key = st.text_input("Enter Groq API Key",value="",type="password")

url = st.text_input("URL",label_visibility="collapsed")


prompt_template = """
Provide summary of the following content in 300 words:
Content:{text}
"""

prompt = PromptTemplate(template=prompt_template,input_variables=['text'])

if st.button("Summarize the content from YT or Website"):
    if not groq_api_key.strip() or not url.strip():
        st.error("Please provide the information")
    elif not validators.url(url):
        st.error("Please enter a valid a valid url.")
    else:
        try:
            with st.spinner("Waiting..."):
                if "youtube.com" in url:
                    loader = YoutubeLoader.from_youtube_url(url,add_video_info=True)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[url],
                        ssl_verify=False,
                        dd_video_info=True,
                        transcript_format=TranscriptFormat.CHUNKS,
                        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
                    )
                docs = loader.load()
                llm = ChatGroq(model="Llama3-8b-8192",groq_api_key=groq_api_key)

                chain = load_summarize_chain(llm=llm,chain_type="stuff",prompt=prompt)
                output_summary = chain.run(docs)

                st.success(output_summary)
        
        except Exception as e:
            st.exception(e)

