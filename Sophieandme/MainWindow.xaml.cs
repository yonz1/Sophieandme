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
using WinInterop = System.Windows.Interop;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Data.SQLite;
using System.Linq;
using System.Security.Cryptography;
using System.Threading.Tasks;
using Microsoft.VisualBasic.ApplicationServices;
using Sophieandme;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ListView;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;
using System.IO;


namespace Sophieandme
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : System.Windows.Window
    {

        [DllImport("dwmapi.dll")]
        private static extern int DwmExtendFrameIntoClientArea(IntPtr hwnd, ref Margins pMarInset);

        [DllImport("dwmapi.dll")]
        private static extern int DwmSetWindowAttribute(IntPtr hwnd, int attr, ref int attrValue, int attrSize);

        private struct Margins
        {
            public int cxLeftWidth;
            public int cxRightWidth;
            public int cyTopHeight;
            public int cyBottomHeight;
        }
        private void MainWindow_Loaded(object sender, RoutedEventArgs e)
        {
            var hwnd = new WindowInteropHelper(this).Handle;
            var margins = new Margins()
            {
                cxLeftWidth = 1,
                cxRightWidth = 1,
                cyTopHeight = 1,
                cyBottomHeight = 1
            };
            DwmExtendFrameIntoClientArea(hwnd, ref margins);

            // Supprimer le coin blanc autour
            int attrValue = 2; // DWMWA_USE_IMMERSIVE_DARK_MODE
            DwmSetWindowAttribute(hwnd, 20, ref attrValue, sizeof(int));
        }


        public MainWindow()
        {
            App.Current.Properties["button_color"] = new SolidColorBrush(System.Windows.Media.Color.FromRgb(0x24, 0x24, 0x24));
            InitializeComponent();
            this.Loaded += MainWindow_Loaded;
            fcontainer.Navigate(new System.Uri("/Pages/Landing.xaml", UriKind.RelativeOrAbsolute));


            App.Current.Properties["html_back"] = "161717";
            App.Current.Properties["html_back_rep"] = "242424";
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

            // FIle.Delete(@"C:\...");
            DirectoryInfo d = new DirectoryInfo(@"../../../HTML");
            FileInfo[] Files = d.GetFiles();
            string str = "";
            foreach ( FileInfo f in Files )
                File.Delete(f.FullName);

            System.Threading.Thread.Sleep(300);
            Application.Current.Shutdown();
        }

        [DllImport("user32.dll")]
        public static extern IntPtr SendMessage(IntPtr hWnd, int wParam, int wMsg, int lParam);


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
            Rect1.Visibility = Visibility.Visible;
            Rect2.Visibility = Visibility.Hidden;
        }
        private void Markedval_Click(object sender, RoutedEventArgs e)
        {
            fcontainer.Navigate(new System.Uri("/Pages/Marked.xaml", UriKind.RelativeOrAbsolute));
            Rect2.Visibility = Visibility.Visible;
            Rect1.Visibility = Visibility.Hidden;
        }
    }
}