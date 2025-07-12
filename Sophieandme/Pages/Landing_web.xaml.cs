using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
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

namespace Sophieandme.Pages
{
    /// <summary>
    /// Logique d'interaction pour Landing_web.xaml
    /// </summary>
    public partial class Landing_web : Page
    {
        public Landing_web()
        {
            InitializeComponent();
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTML_const\\Landing.html";
            urif = urif.Replace("\\", "/");
            System.Uri uri1 = new System.Uri(urif);
            webviewall.Source = uri1 as System.Uri;
        }
    }
}
