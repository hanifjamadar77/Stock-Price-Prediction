import streamlit as st
import pandas as pd

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html= True)
#st.markdown("<h1 style = 'text-align:center;'>URL SHORTENER</h1>",unsafe_allow_html= True)

st.sidebar.image("https://img.freepik.com/free-vector/buy-sell-concept-design-showing-bull-bear_1017-13716.jpg?w=2000")

# DataBase Creation
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_stocktable1():
    c.execute('CREATE TABLE IF NOT EXISTS stocktable1(username TEXT, password TEXT)')

# def delete_usertable():
#     c.execute('DELETE FROM usertable')


def add_stocktable1(username, password):
    if username and password is not None:
        c.execute('INSERT INTO stocktable1(username , password) VALUES (?,?)',(username,password))
        conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM stocktable1 WHERE username =? AND password =?',(username,password))
    data= c.fetchall()
    return data

# def remove_user(username,password):
#     c.execute('SELECT * FROM usertable WHERE username = "" AND password = ""',(username,password))
    
def view_all_user():
    c.execute('SELECT * FROM stocktable')
    data = c.fetchall()
    return data

# import json
# from pathlib import Path
# from streamlit.source_util import _on_pages_changed, get_pages

# Default_page = "Login_page.py"

# def get_all_pages():
#     default_pages = get_pages(Default_page)
#     page_path = Path("pages.json")

#     if page_path.exists():
#         saved_default_pages = json.loads(page_path.read_text)
#     else:
#         saved_default_pages = default_pages.copy()
#         page_path.write_text(json.dumps(default_pages, indent=4))
#     return saved_default_pages

# def clear_all_but_first_page():
#     current_pages = get_pages(Default_page)

#     if len(current_pages.keys())==1:
#         return
    
#     get_all_pages()

#     key,val= list(current_pages.items())[0]
#     current_pages.clear()
#     current_pages[key] = val

#     _on_pages_changed.send()

# def show_all_pages():
#     current_pages = get_pages(Default_page)
#     saved_pages = get_all_pages()
#     missing_keys = set(saved_pages.keys())

#     for key in missing_keys:
#         current_pages[key] = saved_pages[key]

#     _on_pages_changed.send()

# clear_all_but_first_page()


def main():
    st.title("Welcome To Stock Price Prediction")
    menu = ["Login","SignUp"]
    choice = st.selectbox("Menu",menu)


    # Login Page
    if choice == "Login":
        st.subheader("Login Section")

        username = st.text_input("User Name")
        password = st.text_input("Password", type = 'password')
        if st.button("Login"):
    
            create_stocktable1()
            # delete_usertable()
            result = login_user(username,password)
            if result:
              st.success("Logged In as {}".format(username))
              st.info("Go to the Home Page and make your prediction")
            #   remove_user(username,password)
            #   user_result = view_all_user()
            #   clean_db = pd.DataFrame(user_result, columns = ["username","password"])
            #   st.dataframe(clean_db)
            # elif(username == "hanif" and password== "786"):
            #     show_all_pages()

            elif(username == " " ):
                st.warning("Please fill the username field properly")
            elif(password == " "):
                st.warning("Please fill the password field properly")
            else:
                st.warning("Invalid credentials")
                # clear_all_but_first_page()
        else:    
            st.warning("Incorrect Username and Password")
            # clear_all_but_first_page()

    # Sign Up page
    elif choice == "SignUp":
        st.subheader("Create your Account")

        new_user = st.text_input ("Username")
        new_pass = st.text_input("Password", type= "password")
        if st.button("Sign Up"):
            create_stocktable1()
            #remove_user(None,None)

            if new_user and new_pass is not None:
                add_stocktable1(new_user,new_pass)
                st.success("You have successfully created an valid account ")
                st.info("Go to the Home Page and make your prediction")
            
            # elif new_pass is not None:
            #     add_stocktable(new_user,new_pass)
            #     st.success("You have successfully created an valid account ")
            #     st.info("Go to the Home Page and make your prediction")

            else:
                st.warning ("Please fill the fields properly")

        else:    
            st.warning("Incorrect Username and Password")

            

if __name__ == '__main__':
    main()
