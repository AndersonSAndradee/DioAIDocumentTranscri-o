import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analise_credit_card

def configure_interface():
    st.title("Upload de Arquivo Dio. Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        # Enviar para o blob storage

        blob_url = upload_blob(uploaded_file, fileName)

        if blob_url:

            st.write(f'Arquivo {fileName} enviado com sucesso para o azure Blob Storage')
            credit_card_info = analise_credit_card(blob_url) # chamar função de cartão de crédito
            show_image_and_validation(blob_url, credit_card_info)

        else:

            st.write(f'Erro ao enviar o arquivo {fileName} para o Blob Storage')


def show_image_and_validation(blob_url, credit_card_info):

    st.image(blob_url, caption="Imagens enviada", use_container_width= True)
    st.write("Resultado da validação: ")

    if credit_card_info and credit_card_info['card_name']:

        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do titular: {credit_card_info['card_name']}")
        st.write(f"Instituição: {credit_card_info['bank_name']}")
        st.write(f"Data de validade: {credit_card_info['expiry_date']}")
    else:

        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido")



if __name__ == "__main__":

    configure_interface()