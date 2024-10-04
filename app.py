import streamlit as st
import pyttsx3
import tempfile
import os

# Função para listar as vozes disponíveis
def get_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_list = []
    for idx, voice in enumerate(voices):
        voice_list.append((voice.id, voice.name))
    return voice_list

# Função para converter texto em áudio
def text_to_speech(text, voice_id, output_path):
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.save_to_file(text, output_path)
    engine.runAndWait()

def main():
    st.title("Gerador de Audiobook")
    st.write("Converta seu texto em um audiobook com diferentes opções de vozes.")

    # Entrada de texto ou upload de arquivo
    input_method = st.radio("Como você deseja fornecer o texto?", ("Escrever o texto", "Fazer upload de um arquivo de texto (.txt)"))

    if input_method == "Escrever o texto":
        text = st.text_area("Insira o texto aqui:", height=300)
    else:
        uploaded_file = st.file_uploader("Escolha um arquivo de texto", type=["txt"])
        if uploaded_file is not None:
            text = uploaded_file.read().decode('utf-8')
            st.text_area("Texto do arquivo:", text, height=300)
        else:
            text = ""

    # Seleção de voz
    if text:
        st.subheader("Escolha a voz para o audiobook")
        voices = get_voices()
        # Filtrar para garantir pelo menos 3 vozes
        if len(voices) < 3:
            st.warning("Menos de 3 vozes disponíveis no seu sistema.")
        voice_options = {f"{voice[1]} ({voice[0]})": voice[0] for voice in voices[:3]}  # Seleciona as primeiras 3 vozes
        selected_voice = st.selectbox("Voz", list(voice_options.keys()))

        # Botão para gerar o audiobook
        if st.button("Gerar Audiobook"):
            with st.spinner("Gerando o audiobook..."):
                # Usar um arquivo temporário para salvar o áudio
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                    output_path = tmp_file.name

                # Converter o texto em áudio
                text_to_speech(text, voice_options[selected_voice], output_path)

                # Ler o arquivo de áudio para reproduzir no Streamlit
                try:
                    with open(output_path, 'rb') as audio_file:
                        audio_bytes = audio_file.read()

                    # Exibir o player de áudio
                    st.audio(audio_bytes, format='audio/mp3')

                    # Oferecer o download do arquivo
                    st.download_button(
                        label="Baixar Audiobook",
                        data=audio_bytes,
                        file_name='audiobook.mp3',
                        mime='audio/mp3'
                    )
                except Exception as e:
                    st.error(f"Ocorreu um erro ao processar o áudio: {e}")
                finally:
                    # Remover o arquivo temporário
                    try:
                        os.remove(output_path)
                    except Exception as e:
                        st.warning(f"Não foi possível remover o arquivo temporário: {e}")

if __name__ == "__main__":
    main()
