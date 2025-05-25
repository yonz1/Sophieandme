using System;
using System.Collections.Generic;
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
using System.Windows.Shapes;
using Sophieandme;

namespace WpfApp2.Windows
{
    /// <summary>
    /// Logique d'interaction pour Settings.xaml
    /// </summary>
    public partial class Settings : Page
    {
        public Settings()
        {
            InitializeComponent();
        }


        private void Credits_Click(object sender, RoutedEventArgs e)
        {
            fcontainer.Navigate(new System.Uri("/Pages/Settings/Credit.xaml", UriKind.RelativeOrAbsolute));
        }

        private void Contact_Click(object sender, RoutedEventArgs e)
        {
            fcontainer.Navigate(new System.Uri("/Pages/Settings/Contact.xaml", UriKind.RelativeOrAbsolute));
        }

        private void Apps_Click(object sender, RoutedEventArgs e)
        {
            fcontainer.Navigate(new System.Uri("/Pages/Settings/Apps.xaml", UriKind.RelativeOrAbsolute));
        }

        private void Security_Click(object sender, RoutedEventArgs e)
        {
            fcontainer.Navigate(new System.Uri("/Pages/Settings/Security.xaml", UriKind.RelativeOrAbsolute));
        }

        private void General_Click(object sender, RoutedEventArgs e)
        {
            fcontainer.Navigate(new System.Uri("/Pages/Settings/General.xaml", UriKind.RelativeOrAbsolute));
        }

        private void Page_Loaded(object sender, RoutedEventArgs e)
        {
            Usernamebox.Text = App.Current.Properties["username"] as string;
        }
    }
}
