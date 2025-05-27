using Sophieandme;
using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using WpfApp2.Windows;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;

namespace WpfApp2.Pages.Settings
{
    /// <summary>
    /// Logique d'interaction pour Security.xaml
    /// </summary>
    public partial class Security : Page
    {
        public Security()
        {
            InitializeComponent();
        }

        private void logout_Click(object sender, RoutedEventArgs e)
        {
            
            string conSource = "Data Source=..\\..\\..\\user_value.db";
            using (SQLiteConnection c = new SQLiteConnection(conSource))
            {
                c.Open();
                string query = "UPDATE Users SET Keepalive = 0 where Username = \"" + App.Current.Properties["username"] + "\"";
                using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                {
                    cmd.ExecuteNonQuery();
                    Window win = new login();
                    var w = Application.Current.Windows[0];
                    w.Close();
                    win.Show();
                }
            }
        }
    }
}
