using System.Runtime.InteropServices;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Interop;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Sophieandme
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Minimize_Click(object sender, RoutedEventArgs e)
        {
            WindowState = WindowState.Minimized;
        }

        private void Maximize_Click(object sender, RoutedEventArgs e)
        {
            if (WindowState == WindowState.Normal)
                WindowState = WindowState.Maximized;
            else
                WindowState = WindowState.Normal;
        }

        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }
        [DllImport("user32.dll")]
        public static extern IntPtr SendMessage(IntPtr hWnd, int wParam, int wMsg, int lParam);


        private void DockPanel_MouseDown(object sender, MouseButtonEventArgs e)
        {
            WindowInteropHelper helper = new WindowInteropHelper(this);
            SendMessage(helper.Handle, 161, 2, 0);
        }

        private void Grid_MouseDown(object sender, MouseButtonEventArgs e)
        {
            WindowInteropHelper helper = new WindowInteropHelper(this);
            SendMessage(helper.Handle, 161, 2, 0);
        }

        private void Settings_Click(object sender, RoutedEventArgs e)
        {
            fcontainer.Navigate(new System.Uri("/Pages/Settings.xaml", UriKind.RelativeOrAbsolute));
        }

        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            Userbtncontent.Text = App.Current.Properties["username"] as string;
            if (App.Current.Properties["photo"].ToString() == "")
            {
                //Profileellipse.Fill = Profilepicture;
                App.Current.Properties["photo"] = "\\Ryan-Gosling_0.jpg";
                ProfilePict.ImageSource = new BitmapImage(new Uri(App.Current.Properties["photo"].ToString(), UriKind.Relative));
            }
            else
            {
                ProfilePict.ImageSource = new BitmapImage(new Uri(App.Current.Properties["photo"].ToString(), UriKind.Relative));
            }
        }

        private void Quizz_Click(object sender, RoutedEventArgs e)
        {
            fcontainer.Navigate(new System.Uri("/Pages/Quizz.xaml", UriKind.RelativeOrAbsolute));
        }
    }
}