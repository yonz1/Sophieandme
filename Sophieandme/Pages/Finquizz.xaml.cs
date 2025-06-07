using Microsoft.Web.WebView2.Core;
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
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Sophieandme.Pages
{
    /// <summary>
    /// Logique d'interaction pour Finquizz.xaml
    /// </summary>
    public partial class Finquizz : Page
    {
        public Finquizz()
        {
            InitializeComponent();
        }
        private async void webviewques_NavigationCompleted(object sender, Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs e)
        {
            ajustehautevaleur(sender, e);
        }

        private async void webviewrep_NavigationCompleted(object sender, Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs e)
        {

            ajustehautevaleur(sender, e);

        }

        private async Task ajustehautevaleur(object sender, CoreWebView2NavigationCompletedEventArgs e)
        {
            try
            {
                Microsoft.Web.WebView2.Wpf.WebView2 mywebview = sender as Microsoft.Web.WebView2.Wpf.WebView2;
                string result = await mywebview.ExecuteScriptAsync("document.body.scrollHeight.toString()");
                if (int.TryParse(result.Trim('"'), out int height))
                {
                    mywebview.Height = height + 50;
                    System.Diagnostics.Debug.WriteLine(height);
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine(ex.Message);
            }
        }
    }
}
