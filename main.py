import streamlit as st
from zxcvbn import zxcvbn
from streamlit_extras.metric_cards import style_metric_cards

def check_password_strength(password):
    """Check the strength of a given password using zxcvbn."""
    if not password:
        return None

    result = zxcvbn(password)  # Fixed function call
    score = result["score"]  # Score: 0 (Weak) to 4 (Strong)
    feedback = result["feedback"]

    return score, feedback

def get_meter_color(score):
    """Return a color based on password strength score."""
    colors = ["#ff4d4d", "#ff9900", "#ffd633", "#99cc33", "#33cc33"]
    return colors[score]

def main():
    """Streamlit Password Strength Meter App."""
    st.set_page_config(page_title="Password Strength Meter", layout="centered")
    st.title("🔒 Password Strength Meter")
    st.write("Check how strong your password is and get suggestions for improvement.")

    password = st.text_input("Enter your password", type="password")
    
    if password:  # Ensure password is entered before checking strength
        strength_data = check_password_strength(password)

        if strength_data:
            score, feedback = strength_data
            meter_color = get_meter_color(score)
            strength_labels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]

            # Display Password Strength
            st.markdown(f"### Strength: **{strength_labels[score]}**")
            st.progress((score + 1) / 5)

            # Display Score and Status
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Score", score, delta_color="off")
            with col2:
                st.metric("Status", strength_labels[score], delta_color="off")

            # Style metric cards
            style_metric_cards(border_left_color=meter_color)

            # Suggestions for Improvement
            if feedback["suggestions"]:
                st.warning("**Suggestions to Improve:**")
                for suggestion in feedback["suggestions"]:
                    st.write(f"- {suggestion}")
        else:
            st.error("Error processing password strength.")

if __name__ == "__main__":
    main()


# Footer
st.markdown("---")
st.markdown(
    '<p class="footer">🚀 Made by Syed Ahsan | © 2025 All Rights Reserved</p>',
    unsafe_allow_html=True
)
