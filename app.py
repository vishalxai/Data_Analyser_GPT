import streamlit as st
import asyncio
import os
import glob
from teams.analyzer_team import get_analyzer_team

# 1. UI Setup
st.set_page_config(page_title="AI Data Analyst", layout="wide")
st.title("📊 Autonomous AI Data Analyst")
st.markdown("Upload a CSV and let the AI team analyze it, write code, and generate charts.")

# Ensure temp folder exists
os.makedirs("temp", exist_ok=True)

# 2. File Upload
uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])

if uploaded_file is not None:
    # Save the uploaded file directly into the temp directory
    file_path = os.path.join("temp", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' is ready for analysis!")

    # 3. Task Input
    default_prompt = f"""Read the dataset '{uploaded_file.name}'.
I need you to act as a Business Intelligence Analyst.
1. Calculate the total 'Sales' for each 'Region'.
2. Plot a bar chart showing the total sales by region. Make it look professional.
3. Save the chart directly to the current directory as 'regional_sales.png'. Do not use 'temp/' in the path."""

    user_query = st.text_area("Ask the AI Team a question:", value=default_prompt, height=150)

    # 4. Run Analysis Button
    if st.button("🚀 Run Analysis"):
        
        # Clean up old charts before starting so we don't show old data
        for old_png in glob.glob("temp/*.png"):
            os.remove(old_png)

        with st.spinner("🧠 The AI Team is writing code and analyzing data. Please wait..."):
            
            # AutoGen requires async, so we wrap it
            async def run_ai_team():
                team = get_analyzer_team()
                # Run the team and wait for the final result
                result = await team.run(task=user_query)
                return result
            
            # Execute the async function
            final_result = asyncio.run(run_ai_team())
            
            st.divider()
            st.subheader("📝 Final Analyst Report")
            
            # Extract and display the Analyst's final message
            for msg in final_result.messages:
                if getattr(msg, 'source', '') == "Data_Analyst":
                    st.write(msg.content.replace("TERMINATE", ""))

            # Dynamically find and display any new images generated in the temp folder
            png_files = glob.glob("temp/*.png")
            if png_files:
                st.subheader("📈 Generated Visualization")
                # Get the most recently created image
                latest_file = max(png_files, key=os.path.getctime)
                st.image(latest_file)