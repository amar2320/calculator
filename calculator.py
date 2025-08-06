import streamlit as st

st.title("📘 Student Attendance Calculator")

# Input Section
total_classes = st.number_input("Total number of classes conducted", min_value=1)
attended_classes = st.number_input("Number of classes you attended", min_value=0, max_value=total_classes)

if st.button("Calculate Attendance"):
    if total_classes == 0:
        st.error("Total classes can't be zero!")
    else:
        # Calculate percentage
        percentage = (attended_classes / total_classes) * 100
        st.success(f"✅ Your attendance is: {percentage:.2f}%")

        # Check if safe or not
        if percentage >= 75:
            st.info("You are Safe! 🎉")

            # Calculate how many more classes you can bunk
            bunkable = (attended_classes - 0.75 * total_classes) / 0.75
            st.info(f"You can still bunk **{int(bunkable)}** more classes and stay above 75%")
        else:
            st.warning("Short Attendance! ⚠️")

            # Calculate how many more classes are needed
            needed_classes = ((0.75 * total_classes) - attended_classes) / 0.25
            st.warning(f"You need to attend at least **{int(needed_classes) + 1}** more classes to reach 75%")
