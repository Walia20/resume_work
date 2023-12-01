import streamlit as st
import numpy as np
import os
import pandas as pd
from phase1 import header_section
from phase2 import show_projects, real_projects
from phase3 import show_skills
from phase4 import worked_out_experience

sess= st.session_state

if "project_show" not in sess:
    sess["project_show"]=False

header_section()
# show_projects()
real_projects()
show_skills()
worked_out_experience()
