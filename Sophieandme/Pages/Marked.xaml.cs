using CommonWin32.API;
using CSharpMath.Forms;
using FontAwesome.Sharp;
using Microsoft.Web.WebView2.Core;
using Sophieandme.Window;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SQLite;
using System.Diagnostics;
using System.Diagnostics.Metrics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Timers;
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
using static XamlMath.Rendering.Transformations.Transformation;

namespace Sophieandme.Pages
{
    /// <summary>
    /// Logique d'interaction pour Marked.xaml
    /// </summary>
    public partial class Marked : Page
    {
        // ##################################################################################################### Liste utiliser pour le quizz
        // ##################################################################### Liste utiliser aprés mélange
        List<string> Name = new List<string>();
        List<string> question = new List<string>();
        List<string> repnse = new List<string>();
        List<string> url_question = new List<string>();
        List<string> url_rep = new List<string>();
        List<string> Markedinf = new List<string>();



        // ############################################################## Liste compléter par la base de données
        List<string> Aquestion = new List<string>();
        List<string> Arepnse = new List<string>();
        List<string> Aurl_question = new List<string>();
        List<string> Aurl_rep = new List<string>();
        List<string> AMarked = new List<string>();
        int i = 0;

        // ##################################################################################################### Liste utiliser pour l'afffichage directe 

        List<string> questionaf = new List<string>();
        List<string> reponseaf = new List<string>();
        List<string> url_questionaf = new List<string>();
        List<string> url_repaf = new List<string>();

        List<string> labels_list = ["Maths_label", "Physique_label", "SI_label", "Français_label", "Anglais_label", "Erreurs_label", "Quizz_label", "All_label"];
        private Stopwatch _stopwatch;
        private System.Timers.Timer _timer;
        private const string _startTimeDisplay = "00:00";
        ResourceDictionary res = (ResourceDictionary)App.LoadComponent(new Uri("/Sophieandme;component/Style/ButtonStyle.xaml", UriKind.Relative));

        string conSource = "Data Source=..\\..\\..\\data_restored.db";
        public Marked()
        {
            InitializeComponent();
            toolbar.Width = 240;
            int i = 0;
            tbTime.Text = _startTimeDisplay;
            _stopwatch = new Stopwatch();
            _timer = new System.Timers.Timer(1000);

            _timer.Elapsed += OnTimerElapse;

            _stopwatch.Start();
            _timer.Start();


            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTML_const\\Marked.html";
            urif = urif.Replace("\\", "/");
            System.Diagnostics.Debug.WriteLine(urif);
            System.Uri uri1 = new System.Uri(urif);
            webviewall.Source = uri1 as System.Uri;
        }


        private async void Page_Loaded(object sender, RoutedEventArgs e)
        {
            await webviewall.EnsureCoreWebView2Async(null);
            webviewall.CoreWebView2.WebMessageReceived += WebView_WebMessageReceived;
        }

        private void WebView_WebMessageReceived(object sender, CoreWebView2WebMessageReceivedEventArgs e)
        {
            string json = e.WebMessageAsJson;
            var data = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, object>>(json);
            System.Diagnostics.Debug.WriteLine(data["id"]);
            string val = data["id"].ToString().Replace("\\large", "").Replace("\\(", "$").Replace("\\)", "$");
            string query = "DELETE FROM Marked WHERE REPLACE(question, ' ', '') =  REPLACE(\"" + val + "\", ' ', '')";
            System.Diagnostics.Debug.WriteLine(query);
            using (SQLiteConnection c = new SQLiteConnection(conSource))
            {
                c.Open();
                System.Diagnostics.Debug.WriteLine(query);
                using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                {
                    cmd.ExecuteNonQuery();
                }
            }
        }

            private void OnTimerElapse(object sender, ElapsedEventArgs e)
        {
            App.Current.Dispatcher.Invoke(() => tbTime.Text = _stopwatch.Elapsed.ToString(@"mm\:ss"));
        }


        private void Generatevalue(string mat)
        {
            questionaf.Clear();
            reponseaf.Clear();
            url_questionaf.Clear();
            url_repaf.Clear();
            System.Diagnostics.Debug.WriteLine("Test1");
            Getmarked(mat);
            System.Diagnostics.Debug.WriteLine("Test2");
            send_data(questionaf, reponseaf, url_questionaf, url_repaf);
            
        }

        private void Getmarked(string mat)
        {
            var connection = new SQLiteConnection(conSource);
            string valtoreq = "question,reponse,question_img,reponse_img";
            string query = "";
            List<String> Matier = ["SI", "Anglais", "Français", "Erreurs", "Mathématiques"];

            if (mat == "all")
            {
                query = "SELECT " + valtoreq + " FROM Marked ";
            }
            else
            {
                query = "SELECT " + valtoreq + " FROM Marked where Matier = \"" + mat  + "\"" ;
            }
            System.Diagnostics.Debug.WriteLine(query);
            try
            {
                connection.Open();
                System.Diagnostics.Debug.WriteLine(query);
                var command = new SQLiteCommand(query, connection);
                var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    questionaf.Add(miseneformetext(reader.GetString(0)));
                    reponseaf.Add(miseneformetext(reader.GetString(1)));
                    url_questionaf.Add(miseneformetext(reader.GetString(2)));
                    url_repaf.Add(miseneformetext(reader.GetString(3)));
                }
                foreach (string question in question)
                {
                    System.Diagnostics.Debug.WriteLine(question);
                }
            }
            catch (Exception ex)
            {
            }
            connection.Close();
        }

        public static string miseneformetext(string text)
        {
            string question = text.Replace("$", "$$").Replace("$$$", "$").Replace("\\/", "/").Replace("<", "\\lt ").Replace(">", "\\gt ").Replace("\n", "<br>");
            string valeurDebut = " \\( \\large ";
            string valeurFin = "\\) ";
            string questionf = "";
            string pattern = @"\$\$(.*?)\$\$";
            questionf = Regex.Replace(question, pattern, match =>
            {
                string contenu = match.Groups[1].Value;
                return valeurDebut + contenu + valeurFin;
            });
            return questionf;
        }


        private void Showbutton(object sender)
        {
            ButtonContainer.Children.Clear();
            Name.Clear();
            var connection = new SQLiteConnection(conSource);
            List<string> Matier = ["Physique","SI", "Anglais", "Français", "Erreurs", "Mathématiques"];
            try
            {
                connection.Open();
                foreach (string matier in Matier)
                {
                    string query = "SELECT COUNT(*) FROM Marked WHERE Matier = \"" + matier +  "\"";
                    System.Diagnostics.Debug.WriteLine(query);
                    var command = new SQLiteCommand(query, connection);
                    var reader = command.ExecuteReader();
                    while (reader.Read())
                    {
                        int y = reader.GetInt16(0);
                        System.Diagnostics.Debug.WriteLine(y,matier);
                        if (y >= 1)
                        {
                            Name.Add(matier);
                            System.Diagnostics.Debug.WriteLine("Pris");
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                //Testbox.Items.Add(e.ToString());
            }


            foreach(string matier in Name)
            {
                System.Diagnostics.Debug.WriteLine(matier);
            }
            ChargerButton(Name, sender);
            connection.Close();
        }


        private void Resppaper_Click(object sender, RoutedEventArgs e)
        {
            System.Windows.Window win = new Response_paper();
            win.Show();
        }

        private async void webviewques_NavigationCompleted(object sender, Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs e)
        {
            ajustehautevaleur(sender, e);
        }

        private async void webviewrep_NavigationCompleted(object sender, Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs e)
        {

            ajustehautevaleur(sender, e);

        }

        private void stopwatchlogic()
        {
            _stopwatch.Stop();
            _timer.Stop();
            _stopwatch.Reset();
        }

        private void Next_button_Click(object sender, RoutedEventArgs e)
        {
            i++;
            if (i == question.Count)
            {
                i = 0;
                Question.Visibility = Visibility.Collapsed;
                Endquizz.Visibility = Visibility.Visible;
            }
            else
            {
                //Count_text.Text = i.ToString() + "/" + id.Count.ToString() ;
                questionform(i);
                //System.Diagnostics.Debug.WriteLine(i.ToString());
            }


        }

        private void Back_btn_Click(object sender, RoutedEventArgs e)
        {
            Selection.Visibility = Visibility.Visible;
        }

        private void Timer_Checked(object sender, RoutedEventArgs e)
        {
            tbTime.Visibility = Visibility.Visible;
            toolbar.Width = 310;
        }

        private void Timer_Unchecked(object sender, RoutedEventArgs e)
        {
            tbTime.Visibility = Visibility.Collapsed;
            toolbar.Width = 240;
        }

        private void Direct_rep_Click(object sender, RoutedEventArgs e)
        {
            stopwatchlogic();
            Endquizz.Visibility = Visibility.Collapsed;
            allresp.Visibility = Visibility.Visible;
            Question.Visibility = Visibility.Collapsed;
            tbTime.Visibility = Visibility.Collapsed;
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTML\\Resp" + App.Current.Properties["nameindex"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":", "").Replace(".", "") + ".html";
            urif = urif.Replace("\\", "/");
            System.Uri uri1 = new System.Uri(urif);
            if (File.Exists(urif))
            {
                System.Diagnostics.Debug.WriteLine("Il existe");
                webviewall_data.Source = uri1 as System.Uri;
                System.Diagnostics.Debug.WriteLine("Source webview : ", webviewall.Source);
            }
            else
            {
                Allresp();
                webviewall_data.Source = uri1 as System.Uri;
                System.Diagnostics.Debug.WriteLine("Source webview : ", webviewall.Source);
            }
        } 

        private void ViewResp_Click(object sender, RoutedEventArgs e)
        {
            tbTime.Visibility = Visibility.Collapsed;
            Endquizz.Visibility = Visibility.Collapsed;
            allresp.Visibility = Visibility.Visible;
            toolbar.Width = 240;
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Resp" + App.Current.Properties["nameindex"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":", "").Replace(".", "") + ".html";
            //string path = System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Resp" + App.Current.Properties["nameindex"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":", "").Replace(".", "") + ".html";
            urif = urif.Replace("\\", "/");;
            System.Uri uri1 = new System.Uri(urif);
            if (File.Exists(urif))
            {
                System.Diagnostics.Debug.WriteLine("Il existe");
                webviewall_data.Source = uri1 as System.Uri;
                System.Diagnostics.Debug.WriteLine("Source webview : ", webviewall.Source);
            }
            else
            {
                Allresp();
                webviewall_data.Source = uri1 as System.Uri;
                System.Diagnostics.Debug.WriteLine("Source webview : ", webviewall.Source);
            }
        }

        private void Return_Click(object sender, RoutedEventArgs e)
        {
            stopwatchlogic();
            i = 0;
            Question.Visibility = Visibility.Collapsed;
            Selection.Visibility = Visibility.Visible;
            allresp.Visibility = Visibility.Collapsed;
            tbTime.Visibility = Visibility.Collapsed;
            toolbar.Width = 240;
            Endquizz.Visibility = Visibility.Collapsed;
            Name.Clear();
            ButtonContainer.Children.Clear();
        }

        private void Restart_Click(object sender, RoutedEventArgs e)
        {
            stopwatchlogic();
            retrievequizz(App.Current.Properties["nameindex"].ToString());
            shuffle();
            questionform(i);
            toolbar.Width = 240;
            Endquizz.Visibility = Visibility.Collapsed;
            tbTime.Visibility = Visibility.Collapsed;
        }

        private void Back_quizz_Click(object sender, RoutedEventArgs e)
        {

            stopwatchlogic();
            i = 0;
            Question.Visibility = Visibility.Collapsed;
            Selection.Visibility = Visibility.Visible;
            allresp.Visibility = Visibility.Collapsed;
            toolbar.Width = 240;
            tbTime.Visibility = Visibility.Collapsed;
            List<string> Matier = ["Maths", "Physique", "SI", "All"];
            Name.Clear();
            ButtonContainer.Children.Clear();
        }

        private async void Reponse_button_Click(object sender, RoutedEventArgs e)
        {
            webviewrep.Visibility = Visibility.Visible;
            string urif = "";
            create(repnse[i].ToString(), i, "r");

            if (i == 0)
            {
                //urif = "file:///C:/Users/Bastien/source/repos/Sophieandme/Sophieandme/HTML/Mathtr.html";
                urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Mathtr.html";
                urif = urif.Replace("\\", "/");
            }
            else if (i % 2 == 0)
            {
                //urif = "file:///C:/Users/Bastien/source/repos/Sophieandme/Sophieandme/HTML/Math0r.html";
                urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Math0r.html";
                urif = urif.Replace("\\", "/");
            }
            else
            {
                //urif = "file:///C:/Users/Bastien/source/repos/Sophieandme/Sophieandme/HTML/Math1r.html";
                urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Math1r.html";
                urif = urif.Replace("\\", "/");
            }
            System.Diagnostics.Debug.WriteLine(" ################# reponse url : ", urif);
            System.Uri uri1 = new System.Uri(urif);
            webviewrep.Source = uri1 as System.Uri;
            Reponse_button.Visibility = Visibility.Collapsed;
            Next_button.Visibility = Visibility.Visible;
        }




        //############################################################################################################## Fonction utile qui n'intéragissent pas avec l'interface



        private void ChargerButton(List<string> Name, object sender)
        {
            System.Windows.Controls.RadioButton boutonCLique = sender as System.Windows.Controls.RadioButton;
            boutonCLique.IsChecked = false;
            var style = (System.Windows.Style)res["button_quizz_desi"];
            foreach (var namequizz in Name)
            {

                System.Windows.Controls.Button btn = new System.Windows.Controls.Button
                {
                    Content = namequizz,
                    Margin = new System.Windows.Thickness(50, 10, 10, 10),
                    Tag = namequizz,
                    Width = 250,
                    Height = 50,
                    Foreground = System.Windows.Media.Brushes.White,
                    Style = style,
                    FontSize = 14,
                    BorderBrush = App.Current.Properties["button_color"] as SolidColorBrush,
                    Background = App.Current.Properties["button_color"] as SolidColorBrush,
                };

                btn.Click += Bouton_click;

                ButtonContainer.Children.Add(btn);
            }

        }


        private void Bouton_click(object sender, RoutedEventArgs e)
        {
            System.Windows.Controls.Button boutonCLique = sender as System.Windows.Controls.Button;
            string valeur = boutonCLique?.Tag as string;
            _stopwatch.Reset();
            _stopwatch.Start();
            _timer.Start();
            string nameindex = valeur;
            System.Diagnostics.Debug.WriteLine(nameindex);
            App.Current.Properties["nameindex"] = nameindex;
            retrievequizz(nameindex);
            shuffle();
            questionform(i);
        }

        private void Allresp()
        {
            string start = "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\r\n   <style>\r\n  img{\r\n  max-width: 60%;\r\n  max-height: 60%;\r\n  max-height: 7cm;\r\n  margin-top: 0.4cm;\r\n  border-radius: 3%;\r\n} .card {\r\n    margin-top: 0.2cm;\r\n     margin-left: 0.2cm;  \r\n box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);\r\n  transition: 0.3s;\r\n    background-color: #" + App.Current.Properties["html_back_rep"] + ";\r\n   width: 40%;\r\n  border-radius: 5px;\r\n  display: inline-block;\r\n  max-width: 13cm;\r\n}\r\n\r p {\r\n    color: white;\r\n    padding: 0.2cm;\r\n  }\r\n   \n.card:hover {\r\n  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);\r\n}\r\n\r\n\r\n.container {\r\n  padding: 2px 16px;\r\n}" + "body {\r\n    color: #" + App.Current.Properties["html_back_rep"] + ";\r\n    background-color: #" + App.Current.Properties["html_back"] + ";\r\n}\r\n" + " \r\n</style>\r\n</head>\r\n<body> <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js\"> </script> \r\n ";

            for (int i = 0; i < question.Count; i++)
            {
                if (url_question[i] == "" && url_rep[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n    <p>" + miseneformetext(question[i]) + "</p> \r\n <hr>\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                    
                }
                else if (url_question[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n   <p>" + miseneformetext(question[i]) + "</p> \r\n  <hr>\r\n   <img src=\"" + url_rep[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                    
                }
                else if (url_rep[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n   <img src=\"" + url_question[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(question[i]) + "</p> \r\n  <hr>\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                    
                }
                else
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n   <img src=\"" + url_question[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(question[i]) + "</p> \r\n  <hr>\r\n   <img src=\"" + url_rep[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                    
                }
            }
            start += "</body>\r\n</html> \r\n";
            string path = System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTML\\Resp" + App.Current.Properties["nameindex"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":", "").Replace(".", "") + ".html";
            path = path.Replace("/", "\\");
            System.Diagnostics.Debug.WriteLine("Source écrite",path);
            File.WriteAllText(path, start);

        }

        private void shuffle()
        {
            question.Clear();
            repnse.Clear();
            Markedinf.Clear();
            url_question.Clear();
            url_rep.Clear();
            var random = new Random();
            var indices = new List<int>();
            for (int i = 0; i < Aquestion.Count; i++)
            {
                indices.Add(i);
            }
            for (int i = indices.Count - 1; i > 0; i--)
            {
                int j = random.Next(i + 1);
                int temp = indices[i];
                indices[i] = indices[j];
                indices[j] = temp;
            }
            foreach (int i in indices)
            {
                System.Diagnostics.Debug.WriteLine(i.ToString());
            }
            foreach (int i in indices)
            {
                System.Diagnostics.Debug.WriteLine("################################################ Premiére serie d'ajout : ", i.ToString());
                question.Add(Aquestion[i]);
                repnse.Add(Arepnse[i]);
                url_question.Add(Aurl_question[i]);
                url_rep.Add(Aurl_rep[i]);
            }
            System.Diagnostics.Debug.WriteLine("Test3");
        }

        private void retrievequizz(string nameindex)
        {
            var connection = new SQLiteConnection(conSource);
            string query = "";
            if (App.Current.Properties["matier"] == "all")
            {
                query = "SELECT question,reponse, question_img,reponse_img FROM Marked";
                App.Current.Properties["matier"] = nameindex;
            }

            else
            {
                System.Diagnostics.Debug.WriteLine(App.Current.Properties["matier"]);
                System.Diagnostics.Debug.WriteLine(nameindex);
                query = "SELECT question,reponse, question_img,reponse_img FROM MARKED WHERE Matier= \"" + nameindex + "\"";
                System.Diagnostics.Debug.WriteLine(query);
            }


            try
            {
                connection.Open();
                var command = new SQLiteCommand(query, connection);
                var reader = command.ExecuteReader();
                Aquestion.Clear();
                Arepnse.Clear();
                Aurl_question.Clear();
                Aurl_rep.Clear();
                AMarked.Clear();
                while (reader.Read())
                {
                    Aquestion.Add(reader.GetString(0));
                    Arepnse.Add(reader.GetString(1));
                    Aurl_question.Add(reader.GetString(2));
                    Aurl_rep.Add(reader.GetString(3));
                }
            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.ToString());
                System.Diagnostics.Debug.WriteLine(ex.ToString());
            }
        }






        // ################################################################################################################### Fonction de formation des questions
        private async void questionform(int i)
        {
            Question.Visibility = Visibility.Visible;
            Selection.Visibility = Visibility.Collapsed;
            webviewques.Visibility = Visibility.Visible;
            Reponse_button.Visibility = Visibility.Visible;
            webviewrep.Visibility = Visibility.Collapsed;
            Next_button.Visibility = Visibility.Collapsed;
            Selection.Visibility = Visibility.Collapsed;
            Count_text.Text = (i + 1).ToString() + "/" + question.Count.ToString();
            Question.Visibility = Visibility.Visible;
            System.Diagnostics.Debug.WriteLine("#################################### question brut");
            System.Diagnostics.Debug.WriteLine(question[i].ToString());
            create(question[i].ToString(), i, "q");
            List<string> countword = question[i].Split(' ').ToList();


            string urif = "";

            if (i == 0)
            {
                //urif = "file:///C:/Users/Bastien/source/repos/Sophieandme/Sophieandme/HTML/Mathtq.html";
                urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Mathtq.html";
                urif = urif.Replace("\\", "/");

            }

            else if (i % 2 == 0)
            {
                //urif = "file:///C:/Users/Bastien/source/repos/Sophieandme/Sophieandme/HTML/Math0q.html";
                urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Math0q.html";
                urif = urif.Replace("\\", "/");
            }
            else
            {
                //urif = "file:///C:/Users/Bastien/source/repos/Sophieandme/Sophieandme/HTML/Math1q.html";
                urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Math1q.html";
                urif = urif.Replace("\\", "/");
            }
            System.Diagnostics.Debug.WriteLine(" ################# question url : ", urif);
            System.Uri uri1 = new System.Uri(urif);
            webviewques.Source = uri1 as System.Uri;

        }

        private void create(string text, int i, string qor)
        {
            string questionf = miseneformetext(text);
            string htmlval = "";
            string path = "";
            string imgurl = "";
            System.Diagnostics.Debug.WriteLine("#################################### question modifier html");
            System.Diagnostics.Debug.WriteLine(questionf);
            if (qor == "q")
            {
                if (url_question[i] == "")
                {
                    imgurl = "";

                    webviewques.Height = 150;
                    htmlval = "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n  <meta charset=\"utf-8\">\r\n  <meta name=\"viewport\" content=\"width=device-width\">\r\n  <title>MathJax example</title>\r\n  <style>\r\n    p {\r\n    color: white;\r\n    padding: 0.2cm;\r\n  }\r\n  </style>\r\n  <style>\r\n        body {\r\n      background: #" + App.Current.Properties["html_back"] + ";\r\n    }\r\n  </style>\r\n</head>\r\n  <body>\r\n  <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js\"> </script> \r\n <script>\r\nwindow.MathJax = {\r\n  tex: {\r\n    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],\r\n    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]\r\n  },\r\n  options: {\r\n    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],\r\n    renderActions: {\r\n      addMenu: [] // désactive le menu contextuel MathJax\r\n    }\r\n  }\r\n};\r\n</script> \r\n <p> " + questionf + " </p>\r\n  </body>    \r\n</html>";

                }
                else
                {
                    imgurl = "<img src=\"" + url_question[i].Replace("\\/", "/") + "\" >";
                    htmlval = "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <meta charset=\"utf-8\">\r\n    <meta name=\"viewport\" content=\"width=device-width\">\r\n    <title>MathJax example</title>\r\n    <style>\r\n        p {\r\n            color: white;\r\n            padding: 0.2cm;\r\n        }\r\n    </style>\r\n    <style>\r\n        body {\r\n            background: #" + App.Current.Properties["html_back"] + ";\r\n        }\r\n\r\n        .container {\r\n            display: grid;\r\n            align-items: center;\r\n            grid-template-columns: 1fr 100fr 1fr;\r\n            column-gap: 5px;\r\n        }\r\n\r\n        img {\r\n            max-width: 350px;\r\n                    max-height: 230px;\r\n        }\r\n\r\n        .text {\r\n            font-size: 17px;\r\n            display: inline;\r\n        }\r\n    </style>\r\n</head>\r\n<body>\r\n    <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js\"></script>\r\n <script>\r\nwindow.MathJax = {\r\n  tex: {\r\n    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],\r\n    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]\r\n  },\r\n  options: {\r\n    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],\r\n    renderActions: {\r\n      addMenu: [] // désactive le menu contextuel MathJax\r\n    }\r\n  }\r\n};\r\n</script>   <div class=\"container\">\r\n  " + imgurl + "\r\n        <div class=\"text\">\r\n            <p> " + questionf + " </p>\r\n        </div>\r\n\r\n    </div>\r\n</body>\r\n</html>";
                    webviewques.Height = 250;
                }
                //webviewques.NavigateToString(htmlval);
            }

            if (qor == "r")
            {
                if (url_rep[i] == "")
                {
                    webviewrep.Height = 250;
                    imgurl = "";
                    htmlval = "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n  <meta charset=\"utf-8\">\r\n  <meta name=\"viewport\" content=\"width=device-width\">\r\n  <title>MathJax example</title>\r\n  <style>\r\n    p {\r\n  background: #" + App.Current.Properties["html_back_rep"] + ";\r\n  color: white;\r\n    padding: 1cm;\r\n  }\r\n  </style>\r\n  <style>\r\n        body {\r\n      background: #" + App.Current.Properties["html_back"] + ";\r\n    }\r\n  </style>\r\n</head>\r\n  <body>\r\n  <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js\"> </script> \r\n <script>\r\nwindow.MathJax = {\r\n  tex: {\r\n    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],\r\n    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]\r\n  },\r\n  options: {\r\n    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],\r\n    renderActions: {\r\n      addMenu: [] // désactive le menu contextuel MathJax\r\n    }\r\n  }\r\n};\r\n</script>  <p> " + questionf + " </p>\r\n  </body>    \r\n</html>";

                }
                else
                {
                    imgurl = "<img src=\"" + url_rep[i].Replace("\\/", "/") + "\" >";
                    htmlval = "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n    <meta charset=\"utf-8\">\r\n    <meta name=\"viewport\" content=\"width=device-width\">\r\n    <title>MathJax example</title>\r\n    <style>\r\n        p {\r\n            color: white;\r\n            padding: 0.2cm;\r\n        }\r\n    </style>\r\n    <style>\r\n        body {\r\n      background: #" + App.Current.Properties["html_back"] + ";\r\n                      }\r\n\r\n        .container {\r\n    background: #" + App.Current.Properties["html_back_rep"] + ";\r\n    padding: 0.2cm;\r\n     display: grid;\r\n            align-items: center;\r\n            grid-template-columns: 1fr 100fr 1fr;\r\n            column-gap: 5px;\r\n        }\r\n\r\n        img {\r\n            max-width: 350px;\r\n             max-height: 230px;\r\n        }\r\n\r\n        .text {\r\n            font-size: 17px;\r\n            display: inline;\r\n        }\r\n    </style>\r\n</head>\r\n<body>\r\n    <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js\"></script>\r\n  <script>\r\nwindow.MathJax = {\r\n  tex: {\r\n    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],\r\n    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]\r\n  },\r\n  options: {\r\n    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],\r\n    renderActions: {\r\n      addMenu: [] // désactive le menu contextuel MathJax\r\n    }\r\n  }\r\n};\r\n</script>   <div class=\"container\">\r\n  " + imgurl + "\r\n        <div class=\"text\">\r\n            <p> " + questionf + " </p>\r\n        </div>\r\n\r\n    </div>\r\n</body>\r\n</html>";
                    webviewrep.Height = 230;
                }
                //webviewrep.NavigateToString(htmlval);
            }


            System.Diagnostics.Debug.WriteLine(imgurl);

            /// ###############################     Pensez a adapter la couleur de l'arriére plan en fonction du théme choisis 
            ///

            if (i == 0)
            {
                path = "..\\..\\..\\HTMl\\Matht" + qor + ".html";
                File.WriteAllText(path, htmlval);
            }
            else if (i % 2 == 0)
            {
                path = "..\\..\\..\\HTMl\\Math0" + qor + ".html";
                File.WriteAllText(path, htmlval);

            }
            else
            {
                path = "..\\..\\..\\HTMl\\Math1" + qor + ".html";
                File.WriteAllText(path, htmlval);
            }



        }

        private void Updateform(object sender, RoutedEventArgs e)
        {


            System.Windows.Controls.RadioButton boutonCLique = sender as System.Windows.Controls.RadioButton;
            string valeur = boutonCLique?.Tag as string;
            ButtonContainer.Children.Clear();
            Name.Clear();
            App.Current.Properties["matier"] = valeur;
            System.Diagnostics.Debug.Write(valeur.ToString());
            var connection = new SQLiteConnection(conSource);
            List<string> Matier = ["Mathématiques", "Phsique", "SI"];
            try
            {
                connection.Open();
                foreach(string matier in Matier)
                {
                    string query = "SELECT COUNT(*) FROM Maked WHERE Matier = \"" + matier + "\"";
                    var command = new SQLiteCommand(query, connection);
                    var reader = command.ExecuteReader();
                    while (reader.Read())
                    {
                        int y = reader.GetInt16(0);                        
                        if (y > 1)
                        {
                            Name.Append(matier);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                //Testbox.Items.Add(e.ToString());
            }

            ChargerButton(Name, sender);
            connection.Close();
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



        private void SIM_Click(object sender, RoutedEventArgs e)
        {
            clear_label("SI_label", this);
            Generatevalue("SI");
            webviewall.Visibility = Visibility.Visible;
            ButtonContainer.Visibility = Visibility.Collapsed;
        }

        private void AllM_Click(object sender, RoutedEventArgs e)
        {
            clear_label("All_label", this);
            Generatevalue("all");

            webviewall.Visibility = Visibility.Visible;
            ButtonContainer.Visibility = Visibility.Collapsed;
        }

        private void PhysiqueM_Click(object sender, RoutedEventArgs e)
        {
            clear_label("Physique_label", this);
            Generatevalue("Physique");
            webviewall.Visibility = Visibility.Visible;
            ButtonContainer.Visibility = Visibility.Collapsed;
        }

        private void MathsM_Click(object sender, RoutedEventArgs e)
        {
            clear_label("Maths_label", this);
            Generatevalue("Mathématiques");


            webviewall.Visibility = Visibility.Visible;
            ButtonContainer.Visibility = Visibility.Collapsed;
        }

        private void Quizz_Click(object sender, RoutedEventArgs e)
        {
            clear_label("Quizz_label", this);
            Showbutton(sender);
            webviewall.Visibility = Visibility.Collapsed;
            ButtonContainer.Visibility = Visibility.Visible;

        }


        private void Français_Checked(object sender, RoutedEventArgs e)
        {
            clear_label("Français_label", this);
            Generatevalue("Français");
            webviewall.Visibility = Visibility.Visible;
            ButtonContainer.Visibility = Visibility.Collapsed;
            
        }

        private void Anglais_Checked(object sender, RoutedEventArgs e)
        {
            clear_label("Anglais_label", this);
            Generatevalue("Anglais");
            webviewall.Visibility = Visibility.Visible;
            ButtonContainer.Visibility = Visibility.Collapsed;
            
        }

        private void Erreur_Checked(object sender, RoutedEventArgs e)
        {
            clear_label("Erreurs_label", this);
            Generatevalue("Erreurs");
            webviewall.Visibility = Visibility.Visible;
            ButtonContainer.Visibility = Visibility.Collapsed;

            
        }

        private async void send_data(List<string> question,List<string> rep,List<string> quest_url,List<string> rep_url)
        { 
            string json = JsonSerializer.Serialize(question);
            string json2 = JsonSerializer.Serialize(rep);
            string json3 = JsonSerializer.Serialize(quest_url);
            string json4 = JsonSerializer.Serialize(rep_url);
            string jsCode = $"createcard({json},{json2},{json3},{json4})";
            System.Diagnostics.Debug.WriteLine(jsCode);
            await webviewall.CoreWebView2.ExecuteScriptAsync(jsCode);
        }

        private void clear_label(string aimlab,FrameworkElement root)
        {
            foreach (var item in labels_list) 
            {
                var label = root.FindName(item) as System.Windows.Controls.Label;
                if (item == aimlab)
                {
                    label.Visibility = Visibility.Visible;    
                }
                else
                {
                    label.Visibility = Visibility.Collapsed;
                }
            }
        }

    }
}
