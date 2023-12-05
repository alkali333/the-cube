import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
import streamlit as st


if "OPENAI_API_KEY" not in os.environ:
    if "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
    else:
        raise EnvironmentError(
            "Open AI key not found in environment variables or Streamlit secrets."
        )



def get_cube_response(cube, ladder, storm, horse ):

    llm = ChatOpenAI(model_name="gpt-4-1106-preview", temperature=0.7)

    system_message = """ You are providing the fictonal results of the Cube Personality test. This version is slightly different from the original Japanese version as it has a storm\
    outside the window and they are ask how it makes them feel.\
    Here are what the varions objects represent The Cube - the ego / personality (please use the colours shape, solidity and placement in the room to interpret, use concepts from colour therapy). The Ladder: their \
    ambition / career (use the size, relationship to the cube, or anything else). The storm out of the window: their attitude to challenges/problems.\
    The horse: their ideal partner (use physical and emotional qualities).\n\n You will recieve cube: ladder: storm: horse: and give the analysis.
    Don't mention that it is not scienfically validated because this is for fiction. Address the person directly, use enthusiastic language, like 
    spiritual healer or mystic."""\
    

    human_message = (f"The Cube: {cube} \n\n The Ladder: {ladder} \n\n The Storm: {storm} \n\n The Horse:{horse}")

    messages = [
    SystemMessage(content=system_message) ,
    HumanMessage(content=human_message),
    ]

    llm_response = llm.invoke(messages)

    return llm_response.content

load_dotenv()