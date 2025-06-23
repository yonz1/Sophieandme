using Microsoft.Web.WebView2.Core;
using System;
using System.Collections.Generic;
using System.Diagnostics;
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
using static CSharpMath.Rendering.Text.TextAtom;

namespace Sophieandme.Pages
{
    /// <summary>
    /// Logique d'interaction pour Custom_quizz.xaml
    /// </summary>
    public partial class Custom_quizz : Page
    {
        ResourceDictionary res = (ResourceDictionary)App.LoadComponent(new Uri("/Sophieandme;component/Style/ButtonStyle.xaml", UriKind.Relative));
        string conSource = "Data Source=..\\..\\..\\data_restored.db";
        List<string> ID = new List<string>();


        public Custom_quizz()
        {
            InitializeComponent();
        }

        private void RadioButton_Click(object sender, RoutedEventArgs e)
        {

        }



        private async void Create_Click_1(object sender, RoutedEventArgs e)
        {

            await webviewall.EnsureCoreWebView2Async(null);
            webviewall.CoreWebView2.WebMessageReceived += WebView_WebMessageReceived;
            Create_grid.Visibility = Visibility.Visible;
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTML_const\\Custom.html";
            urif = urif.Replace("\\", "/");
            System.Uri uri1 = new System.Uri(urif);
            webviewall.Source = uri1 as System.Uri;
        }

        private void WebView_WebMessageReceived(object sender, CoreWebView2WebMessageReceivedEventArgs e)
        {
            string json = e.WebMessageAsJson;   
            var data = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, object>>(json);

            string matier = data["matier"].ToString();
            string nom = data["name"].ToString();
            string question = data["question"].ToString();
            string quest_im = data["quest_img"].ToString();
            string rep = data["rep"].ToString();
            string rep_img = data["rep_img"].ToString();


        }

        private void custom_but_Click(object sender, RoutedEventArgs e)
        {
            Create_grid.Visibility = Visibility.Collapsed;

        }
    }
}
