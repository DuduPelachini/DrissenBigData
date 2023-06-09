import streamlit as st
from deta import Deta

from frontend.src.pages.cadastro import create_account


# Load environment variables
DETA_KEY = "e0zg3sgc85x_rLjU5Zy93MAHEY8UaoCnMGDJSNZiiHNR"

# Initialize Deta
deta = Deta(DETA_KEY)

db = deta.Base("database")


def autenticar_usuario(senha):
    # Lógica de autenticação aqui
    # Se a autenticação for bem-sucedida, redireciona para a página principal
    st.experimental_set_query_params()
    st.experimental_rerun()

def authenticate():
    # Check if the session state has already been set
    if 'authenticated' not in st.session_state:
        # Display login form
        st.title("Authentication")
        password_input = st.text_input("Enter password", type="password")
        login_button = st.button("Log In")

        if st.button("Criar conta"):
            create_account()
        
        else:
            if login_button:
                # Retrieve password from the database
                result = db.get("user")
                
                if result:
                    password = result.get("password")
                    
                    if password_input == password:
                        st.session_state.authenticated = True
                        with st.spinner("Carregando..."):
                            st.success("Login efetuado com sucesso!")
                            st.balloons()
                        # Rerun the script to replace the login page with the main page
                        st.experimental_rerun()
                    else:
                        st.error("Nome de usuário ou senha incorretos.")
                        st.info("Se você esqueceu sua senha, entre em contato com o administrador.")
                else:
                    st.error("Usuário não encontrado.")
                    st.info("Entre em contato com o administrador para obter acesso.")

                st.markdown("""
                <style>
                    .container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    padding: 2rem;
                    }

                    .form-group {
                    width: 100%;
                    margin-bottom: 1rem;
                    }

                    .form-control {
                    width: 100%;
                    padding: 0.75rem;
                    font-size: 1rem;
                    border-radius: 0.25rem;
                    border: 1px solid #ced4da;
                    }

                    .form-control:focus {
                    outline: none;
                    box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
                    border-color: #80bdff;
                    }

                    .btn {
                    display: inline-block;
                    font-weight: 400;
                    color: #212529;
                    text-align: center;
                    vertical-align: middle;
                    user-select: none;
                    background-color: transparent;
                    border: 1px solid transparent;
                    padding: 0.375rem 0.75rem;
                    font-size: 1rem;
                    line-height: 1.5;
                    border-radius: 0.25rem;
                    transition: color 0.15s ease-in-out,
                                background-color 0.15s ease-in-out,
                                border-color 0.15s ease-in-out,
                                box-shadow 0.15s ease-in-out;
                    }

                    .btn-primary {
                        color: #fff;
                        background-color: #007bff;
                        border-color: #007bff;
                    }

                    .btn-primary:hover {
                        color: #fff;
                        background-color: #0069d9;
                        border-color: #0062cc;
                    }

                    .btn-primary:focus {
                        color: #fff;
                        background-color: #0069d9;
                        border-color: #0062cc;
                        box-shadow: 0 0 0 0.2rem rgba(38, 143, 255, 0.5);
                    }
                </style>
                """, unsafe_allow_html=True)

                st.header("Contact")

                contact_form = """
                <div class="container">
                    <form id="contact-form" action="https://formsubmit.co/{}" method="POST">
                    <div class="form-group">
                        <input class="form-control" type="text" name="name" placeholder="Your name" required>
                    </div>
                    <div class="form-group">
                        <input class="form-control" type="email" name="email" placeholder="Your email" required>
                    </div>
                    <div class="form-group">
                        <textarea class="form-control" name="message" placeholder="Your message here"></textarea>
                    </div>
                    <div class="form-group">
                        <button class="btn btn-primary" type="submit" onclick="validateForm(event)">Send</button>
                    </div>
                    </form>
                </div>
                """.format("estevamsouzalaureth@gmail.com")  # Substitua o endereço de e-mail aqui

                javascript_code = """
                <script>
                    function validateForm(event) {
                    var form = document.getElementById('contact-form');
                    var nameInput = form.elements['name'];
                    var emailInput = form.elements['email'];
                    var messageInput = form.elements['message'];

                    if (nameInput.value.trim() === '' || emailInput.value.trim() === '' || messageInput.value.trim() === '') {
                        event.preventDefault();
                        alert('Por favor, preencha todos os campos do formulário.');
                    } else {
                        animateSubmitButton();
                    }
                    }

                    function animateSubmitButton() {
                    var submitButton = document.querySelector('.btn-primary');
                    submitButton.innerHTML = 'Sending...';
                    submitButton.classList.add('animate__animated', 'animate__fadeOut');

                    setTimeout(function() {
                        submitButton.innerHTML = 'Sent!';
                        submitButton.classList.remove('animate__fadeOut');
                        submitButton.classList.add('animate__zoomIn');
                    }, 2000);
                    }
                </script>
                """

                st.markdown(contact_form + javascript_code, unsafe_allow_html=True)