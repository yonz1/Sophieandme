using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Data.SQLite;
using System.Linq;
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Interop;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using Microsoft.VisualBasic.ApplicationServices;
using Sophieandme;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ListView;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;




namespace WpfApp2.Windows
{
    /// <summary>
    /// Logique d'interaction pour login.xaml
    /// </summary>
   
    public partial class login : Window
    {

        string Username = "";
        public login()
        {
            InitializeComponent();

        }


        private void Connect_Click(object sender, RoutedEventArgs e)
        {
            Username = Usernamebox.Text.ToString();
            string Password = PasswordBox.Password.ToString();
            
            //bool? result1 = new customMessageBox(EncryptShA(Password), MessageType.Error, MessageButtons.Ok).ShowDialog();
            Password = EncryptShA(Password);
            if (VerifyUser(Username, Password))
            {
                System.Diagnostics.Debug.WriteLine("############### Passage effectuer");
                string conSource = "Data Source=..\\..\\..\\user_value.db";
                using (SQLiteConnection c = new SQLiteConnection(conSource))
                {
                    c.Open();
                    string query = "SELECT Email,Photo from Users where Username like \"" + Username + "\"";
                    using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                    {
                        using (SQLiteDataReader rdr = cmd.ExecuteReader())
                        {
                            while (rdr.Read())
                            {
                                var email = rdr.GetString(0);
                                var photo = rdr.GetValue(1);
                                App.Current.Properties["email"] = email.ToString();
                                App.Current.Properties["photo"] = photo.ToString();
                                //MessageBox.Show(email.ToString());
                                //MessageBox.Show(photo.ToString());
                            }
                        }
                    }
                }

                if (Stay_con.IsChecked == true)
                {
                    conSource = "Data Source=..\\..\\..\\user_value.db";
                    using (SQLiteConnection c = new SQLiteConnection(conSource))
                    {
                        c.Open();
                        string query = "UPDATE Users set Keepalive = 1 WHERE Username = \"" + Username + "\"";
                        using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                        {
                            cmd.ExecuteNonQuery();
                        }

                    }
                }
                App.Current.Properties["username"] = Username;
                Window win = new MainWindow();
                win.Show();
                this.Close();
            }
            else
            {
                bool? result = new customMessageBox("Incorrect Credentials", MessageType.Error, MessageButtons.Ok).ShowDialog();
            }
            

        }



        private bool VerifyUser(string username, string password)
        {
            string conSource = "Data Source=..\\..\\..\\user_value.db";
            using (SQLiteConnection c = new SQLiteConnection(conSource))
            {
                c.Open();
                string query = "SELECT Username,Password from Users WHERE Username = \"" + username + "\"";
                using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                {
                    using (SQLiteDataReader rdr = cmd.ExecuteReader())
                    {
                        while (rdr.Read())
                        {
                            string usernamerec = rdr.GetString(0);
                            string passwordrec = rdr.GetString(1);
                            System.Diagnostics.Debug.WriteLine("#################################### Utilisatuer dans la base de données : ", usernamerec);
                            if (usernamerec == username && passwordrec == password) 
                            {
                                // Return pareil que VerifyPassword
                                return true;

                            }
                            //bool? result = new customMessageBox(reader.GetString(y), MessageType.Success, MessageButtons.Ok).ShowDialog();
                        }
                    }
                }
            }
            return false;

        }

        private string EncryptShA(string password)
        { 
            var crypt = new System.Security.Cryptography.SHA256Managed();
            var hash = new System.Text.StringBuilder();
            byte[] crypto = crypt.ComputeHash(Encoding.UTF8.GetBytes(password));   
            foreach (byte theByte in crypto)
            {
                hash.Append(theByte.ToString("x2"));
            }
            return hash.ToString();
        }



        // A changer en Bool

        private bool VerifyPasswordSQL(string password, string conSource) 
        { 

            //string query = "SELECT Password from Users";
            //var command = new SQLiteCommand(query, connection);
            //var reader = command.ExecuteReader();
            //while (reader.Read())
            //{
            //    for (int y = 0; y < reader.FieldCount; y++)
            //    {
            //        var value = reader.GetString(y);
            //        System.Diagnostics.Debug.WriteLine("################################# Mot de passe récupérer : ", value);
            //        if (value == password.ToString())
            //        {
            //            connection.Close();
            //            return true; 
            //        }
            //    }
            //}

            using (SQLiteConnection c = new SQLiteConnection(conSource))
            {
                c.Open();
                string query = "SELECT Password from Users";
                using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                {
                    using (SQLiteDataReader rdr = cmd.ExecuteReader())
                    {
                        for (int y = 0; y < rdr.FieldCount; y++)
                        {
                            var value = rdr.GetString(y);
                            System.Diagnostics.Debug.WriteLine("################################# Mot de passe récupérer : ", value);
                            if (value == password.ToString())
                            {
                                c.Close();
                                return true;
                            }
                        }
                    }
                }
            }
            return false ;
        }

        private void Registerform_Click(object sender, RoutedEventArgs e)
        {

        }

        private void Loginform_Click(object sender, RoutedEventArgs e)
        {

        }

        private void Register_Click(object sender, RoutedEventArgs e)
        {
            string email = textBox2.Text.ToString();
            string Username = textBox3.Text.ToString();
            string Password = textBox4.Password.ToString();
            Password = EncryptShA(Password);
            string conSource = "Data Source=..\\..\\..\\user_value.db";
            var connection = new SQLiteConnection(conSource);
            connection.Open();
            string query = "SELECT count(*) from Users where email = " + "\"" + email + "\"";
            //MessageBox.Show(query);
            var command = new SQLiteCommand(query, connection);
            SQLiteDataReader reader = command.ExecuteReader();
            while (reader.Read())
            {
                int number = reader.GetInt16(0);
               // bool? result2 = new customMessageBox(number.ToString(), MessageType.Error, MessageButtons.Ok).ShowDialog();
                if (number != 0)
                {
                    bool? result1 = new customMessageBox("This email is already registered.", MessageType.Error, MessageButtons.Ok).ShowDialog();
                    break;
                }
                if (number == 0)
                {
                    //bool? result3 = new customMessageBox(email, MessageType.Error, MessageButtons.Ok).ShowDialog();
                    //bool? result4 = new customMessageBox(Username, MessageType.Error, MessageButtons.Ok).ShowDialog();
                    //bool? result5 = new customMessageBox(Password, MessageType.Error, MessageButtons.Ok).ShowDialog();
                    try
                    {
                        string Input = "INSERT into Users(Username, Password, Email) VALUES (" +  "\"" + Username + "\"" + "," + "\"" + Password + "\"" +  "," + "\"" +  email + "\"" + ")";
                        //MessageBox.Show(Input.ToString());
                        command = new SQLiteCommand(Input, connection);
                        var test = command.ExecuteNonQuery();
                        //MessageBox.Show(test.ToString());
                        connection.Close();
                        bool? result1 = new customMessageBox("Registration succeed, welcome to Sophieandme", MessageType.Success, MessageButtons.Ok).ShowDialog();
                        textBox2.Text = "";
                        textBox3.Text = "";
                        textBox4.Password = "";
                        break;
                    }
                    catch (Exception ex)
                    {
                        bool? result1 = new customMessageBox("An error as occured during registration, please retry later.", MessageType.Error, MessageButtons.Ok).ShowDialog();
                        //MessageBox.Show(ex.ToString());
                        break;
                    }
                }
            }
        }

        [DllImport("user32.dll")]
        public static extern IntPtr SendMessage(IntPtr hWnd, int wParam, int wMsg, int lParam);

        private void Grid_down_MouseDown(object sender, MouseButtonEventArgs e)
        {
            WindowInteropHelper helper = new WindowInteropHelper(this);
            SendMessage(helper.Handle, 161, 2, 0);
        }

        private void Minimize_Click(object sender, RoutedEventArgs e)
        {
            WindowState = WindowState.Minimized;
        }

        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }

        private void window_Loaded(object sender, RoutedEventArgs e)
        {
            string conSource = "Data Source=..\\..\\..\\user_value.db";
            using (SQLiteConnection c = new SQLiteConnection(conSource))
            {
                c.Open();
                string query = "SELECT Keepalive,Email,Photo,Username FROM Users";
                using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                {
                    using (var rdr = cmd.ExecuteReader())
                    {
                        while (rdr.Read())
                        {
                            var keepalive = rdr.GetValue(0);
                            var email = rdr.GetValue(1);
                            var photo = rdr.GetValue(2);
                            var username = rdr.GetValue(3);
                            if (keepalive.ToString() == "1")
                            {
                                App.Current.Properties["email"] = email.ToString();
                                App.Current.Properties["photo"] = photo.ToString();
                                App.Current.Properties["username"] = username.ToString();
                                Window win = new MainWindow();
                                win.Show();
                                this.Close();
                            }
                        }
                    }
                }
            }
        }
    }
}
