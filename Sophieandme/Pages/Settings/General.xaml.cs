using Microsoft.VisualBasic.ApplicationServices;
using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Forms;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using Sophieandme;
using static System.Data.Entity.Infrastructure.Design.Executor;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;

namespace WpfApp2.Pages.Settings
{
    /// <summary>
    /// Logique d'interaction pour General.xaml
    /// </summary>
    public partial class General : Page
    {
        string choose = "";
        public General()
        {
            InitializeComponent();
        }

        private void edit_name_Click(object sender, RoutedEventArgs e)
        {

        }

        private void edit_email_Click(object sender, RoutedEventArgs e)
        {

        }

        private void edit_theme_Click(object sender, RoutedEventArgs e)
        {

        }


        private void Cancel_name_Click(object sender, RoutedEventArgs e)
        {
            textBox_name.Text = null;
            textBox_email.Text = null;
            Themecombo.SelectedIndex = 1;
        }

        private void Applybtn_name_Click(object sender, RoutedEventArgs e)
        {

        }

        private void Applybtn_email_Click(object sender, RoutedEventArgs e)
        {

        }

        private void Applybtn_theme_Click(object sender, RoutedEventArgs e)
        {

        }

        private void Page_Loaded(object sender, RoutedEventArgs e)
        {
            textBlock_name.Text = App.Current.Properties["username"] as string;
            textBlock_email.Text = App.Current.Properties["email"] as string;
            if (App.Current.Properties["photo"].ToString() == "")
            {
                //Profileellipse.Fill = Profilepicture;
                App.Current.Properties["photo"] = "..\\..\\..\\Ryan-Gosling_0.jpg";
                Profilepicture.ImageSource = new BitmapImage(new Uri(App.Current.Properties["photo"].ToString(), UriKind.Relative));
            }
            else
            {
                Profilepicture.ImageSource = new BitmapImage(new Uri(App.Current.Properties["photo"].ToString(), UriKind.Relative));
            }
        }


        private void PPbtn_Click(object sender, RoutedEventArgs e)
        {
            System.Windows.Forms.OpenFileDialog ofd_transfer = new System.Windows.Forms.OpenFileDialog
            {
                //InitialDirectory = @"C:\",
                Title = " Browse File",

                CheckFileExists = true,
                CheckPathExists = true,
                Filter = "Files|*.jpg;*.jpeg;*.png",
                FilterIndex = 1,
                RestoreDirectory = true,
                ReadOnlyChecked = true,
                ShowReadOnly = true,
            };

            if (ofd_transfer.ShowDialog() == DialogResult.OK)
            {
                Profilepicture.ImageSource = new BitmapImage(new Uri(ofd_transfer.FileName, UriKind.Relative));
                choose = ofd_transfer.FileName;
                //App.Current.Properties["photo"] = ofd_transfer.FileName;
                Validatebtn.Visibility = Visibility.Visible;
                Cancelbtn.Visibility = Visibility.Visible;
            }
        }

        private void Validatebtn_Click(object sender, RoutedEventArgs e)
        {
            Validatebtn.Visibility = Visibility.Hidden;
            Cancelbtn.Visibility = Visibility.Hidden;
            string conSource = "Data Source=..\\..\\..\\user_value.db";
            var connection = new SQLiteConnection(conSource);
            connection.Open();
            string Input = "UPDATE Users set Photo = \"" + choose + "\" where Username = \"" + App.Current.Properties["username"] + "\"" ;
            var command = new SQLiteCommand(Input, connection);
            var test = command.ExecuteNonQuery();
            connection.Close();
        }

        private void Cancelbtn_Click(object sender, RoutedEventArgs e)
        {
            Validatebtn.Visibility = Visibility.Hidden;
            Cancelbtn.Visibility = Visibility.Hidden;
            //App.Current.Properties["photo"] = "..\\..\\..\\Ryan-Gosling_0.jpg";
            Profilepicture.ImageSource = new BitmapImage(new Uri(App.Current.Properties["photo"].ToString(), UriKind.Relative));


        }
    }
}
