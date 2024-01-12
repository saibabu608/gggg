import streamlit as st

st.header('Great Dane')
st.write('Great Dane')

# Use a valid image URL
image_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.petinsurance.com%2Fhealthzone%2Fpet-breeds%2Fdog-breeds%2Fgreat-dane%2F&psig=AOvVaw1VO1hqGVorhL1DBobLA8k7&ust=1705123182673000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCLDd6oGN14MDFQAAAAAdAAAAABAD'

# Display the image with a caption
st.image(image_url, caption='Toyota Supra')

# You can also add alternative text for accessibility
# st.image(image_url, caption='Toyota Supra', alt='Toyota Supra Image')




