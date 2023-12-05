import streamlit as st

from functions import get_cube_response


st.set_page_config(
    page_title="The Cube",
    page_icon=":white_large_square:",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)


st.header(" :brain: The Cube")
st.write(
    """This is a powerful visualisation exercise. Before answering each question, close your eyes and
         spent a few moments picturing the scene in your mind's eye. """
)

with st.form(key="cube"):
    st.write(
        """Imagine you are in an empty room with white walls, the only thing in the room is a cube.
             What colour is it? How about the shape? Is it transparent or solid? Where in the room is it?
             Is there anything else interesting you notice about it?"""
    )
    cube = st.text_area(label="Tell me about the cube.")
    st.write(
        """Now imagine there is a ladder in the room. How big is it? Where is it in relation 
             to the cube? What else do you notice about the ladder?"""
    )
    ladder = st.text_area(label="Tell me about the ladder.")
    st.write(
        """You notice there is now a window in the room. Outside it you can see a storm in 
             the distance. What do you notice about it? How does it make you feel?"""
    )
    storm = st.text_area(label="Tell me about the storm.")
    st.write(
        """Now you can forget everything else, and imagine a horse. How does it look?
             more importantly: what are its personality characteristics."""
    )
    horse = st.text_area(label="Tell me about the horse.")

    submitted = st.form_submit_button("Go")

if submitted and cube and ladder and storm and horse:
    with st.spinner("Analysing... "):
        response = get_cube_response(cube=cube, ladder=ladder, storm=storm, horse=horse)

    st.write(response)
