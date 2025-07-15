import streamlit as st
import pyperclip
from encryption_logic import encrypt_word, decrypt_word, decryption_key, encryption_key, find_index


def encryption_form():
    with st.form('Ecnrypt your message'):
        encrypt = st.text_input('Enter your message', placeholder='...')
        submit = st.form_submit_button('Encrypt Message')
        if submit and encrypt:
            shift_num = find_index(encrypt)
            encrypted_message, index = encrypt_word(encrypt, shift_num)
            key = encryption_key(index)
            pyperclip.copy(key)
            st.markdown(f'Your encrypted message is &mdash; :red[{encrypted_message}]')
            st.markdown(f'Your encryption key has been copied')
            pyperclip.copy(key)
        elif submit and not encrypt:
            st.error('Please enter a message before you press the button')

def decryption_form():
    with st.form('Decrypt your message'):
        decrypt_key = st.text_input('Enter your encryption key', placeholder='paste from clipboard')
        decrypt = st.text_input('Enter your message', placeholder='...')
        submit = st.form_submit_button('Decrypt Message')
        if submit and decrypt and decrypt_key:
            key = decryption_key(int(decrypt_key))
            decrypted_message = decrypt_word(decrypt, key)
            st.markdown(f'Your decrypted message is &mdash; :red[{decrypted_message}]')
        elif submit and not (decrypt and decrypt_key):
            st.error('Please fill in all inputs before submitting')

def main():
    st.title('Ceaser Cipher Encryption')
    st.markdown('## Encryption')
    try:
        encryption_form()
    except ValueError:
        st.error('Make sure everything you entered is in the alphabet')
    st.markdown('## Decryption')
    decryption_form()

main()