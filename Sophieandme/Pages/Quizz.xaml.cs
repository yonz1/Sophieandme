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
using System.Data.SQLite;
using Microsoft.VisualBasic.ApplicationServices;
using System.Data;
using System.Reflection;
using System.Net;
using System.IO;
using WpfMath;
using Aspose.TeX;
using Aspose.TeX.Features;
using Aspose.TeX.Presentation;
using Aspose.TeX.IO;
using WpfMath.Parsers;
using WpfMath;
using XamlMath.Exceptions;
using Typography.OpenFont.Tables;
using System.Text.RegularExpressions;
using System.Windows.Media.Imaging;
using WpfMath.Parsers;
using WpfMath.Rendering;
using XamlMath;
using System.Diagnostics;
using Sophieandme;
using System.Xml.Linq;
using System.Runtime.CompilerServices;
using CSharpMath.Rendering.FrontEnd;
using Microsoft.VisualBasic.ApplicationServices;
using System.Net.Quic;
using Microsoft.Web.WebView2.WinForms;
using Microsoft.Web.WebView2.Wpf;
using System.Diagnostics.Eventing.Reader;
using static CSharpMath.Rendering.Text.TextAtom;
using System.Diagnostics.SymbolStore;
using System.Windows.Threading;
using System.Timers;
using System.Windows.Forms;
using System.Windows;
using System.Windows.Controls.Primitives;
using Sophieandme.Window;
using System.Windows.Media.Animation;
using System.Drawing;
using MaterialDesignThemes.Wpf;
using Microsoft.Web.WebView2.Core;
using System.Windows.Media.Media3D;
using System.Diagnostics.Metrics;
using System.Text.Json;




//C: \Users\Bastien\source\repos\Sophieandme\Sophieandme



namespace Sophieandme.Pages
{
    /// <summary>
    /// Logique d'interaction pour Quizz.xaml
    /// </summary>
    /// 
    public partial class Quizz : System.Windows.Controls.Page
    {
        string conSource = "Data Source=..\\..\\..\\data_restored.db";
        List<string> labels_list = ["Maths_label", "Physique_label", "SI_label", "Français_label", "Anglais_label", "Erreurs_label", "All_label"];


        // ##################################################################### Liste utiliser aprés mélange
        List<string> Name = new List<string>();
        List<string> id = new List<string>();
        List<string> question = new List<string>();
        List<string> repnse = new List<string>();
        List<string> url_question = new List<string>();
        List<string> url_rep = new List<string>();
        List<string> difficulty = new List<string>();
        List<string> Marked = new List<string>();

        // ############################################################## Liste compléter par la base de données
        List<string> AName = new List<string>();
        List<string> Aid = new List<string>();
        List<string> Aquestion = new List<string>();
        List<string> Arepnse = new List<string>();
        List<string> Aurl_question = new List<string>();
        List<string> Aurl_rep = new List<string>();
        List<string> Adifficulty = new List<string>();
        List<string> AMarked = new List<string>();
        int i = 0;

        private Stopwatch _stopwatch;
        private System.Timers.Timer _timer;
        private const string _startTimeDisplay = "00:00";
        ResourceDictionary res = (ResourceDictionary)App.LoadComponent(new Uri("/Sophieandme;component/Style/ButtonStyle.xaml", UriKind.Relative));


        //bool ensure = false;

        //private void webView21_CoreWebView2InitializationCompleted(object sender, Microsoft.Web.WebView2.Core.CoreWebView2InitializationCompletedEventArgs e)
        //{
        //    ensure = true;
        //}



        public Quizz()
        {
            ResourceDictionary Myressodico = new ResourceDictionary();
            InitializeComponent();
            toolbar.Width = 240;
            int i = 0;
            tbTime.Text = _startTimeDisplay;
            _stopwatch = new Stopwatch();
            _timer = new System.Timers.Timer(1000);
            webviewquizz.Visibility = Visibility.Visible;
            _timer.Elapsed += OnTimerElapse;

            _stopwatch.Start();
            _timer.Start();

            marked_list();
        }

        private async void Page_Loaded(object sender, RoutedEventArgs e)
        {
            await webviewquizz.EnsureCoreWebView2Async();
            webviewquizz.CoreWebView2.Settings.IsStatusBarEnabled = false;
            webviewquizz.CoreWebView2.Settings.AreDefaultContextMenusEnabled = false;
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTML_const\\quizz.html";
            urif = urif.Replace("\\", "/");
            System.Uri uri1 = new System.Uri(urif);
            webviewquizz.Source = uri1 as System.Uri;
            System.Diagnostics.Debug.WriteLine(webviewquizz.Source.ToString());
            webviewquizz.CoreWebView2.NavigationCompleted += (sender, args) =>
            {
                webviewquizz.CoreWebView2.ExecuteScriptAsync("console.log('fonctionne');");
                questionform(i, "question");
            };
        }


        private void marked_list()
        {
            string query = "";
            var connection = new SQLiteConnection(conSource);
            query = "SELECT question  FROM Marked";

            try
            {
                connection.Open();
                var command = new SQLiteCommand(query, connection);
                var reader = command.ExecuteReader();
                Marked.Clear();
                while (reader.Read())
                {
                    Marked.Add(reader.GetString(0));
                }
            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.ToString());
                System.Diagnostics.Debug.WriteLine(ex.ToString());
            }
        }

        public void run_cmd(object command)
        {
            System.Diagnostics.ProcessStartInfo procstatinfo = new System.Diagnostics.ProcessStartInfo("cmd", "/c" + command);
            procstatinfo.UseShellExecute = false;
            System.Diagnostics.Debug.WriteLine("Test0");
            procstatinfo.CreateNoWindow = true;
            procstatinfo.RedirectStandardOutput = true;
            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.StartInfo = procstatinfo;
            proc.Start();
        }

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
                    Foreground = App.Current.Properties["button_color_text"] as SolidColorBrush,
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
            webviewquizz.Visibility = Visibility.Visible;
            webviewall.Visibility = Visibility.Collapsed;
            marked_list();
            retrievequizz(nameindex);
            shuffle();
            questionform(i,"question");
        }
        private void OnTimerElapse (object sender, ElapsedEventArgs e)
        {
            App.Current.Dispatcher.Invoke(() => tbTime.Text = _stopwatch.Elapsed.ToString(@"mm\:ss" ));
        }

        // ################################################################################################################### Fonction de formation des questions
        private async void questionform(int i,string action)
        {
            Selection.Visibility = Visibility.Collapsed;
            Count_text.Text = (i + 1).ToString() + "/" + id.Count.ToString();
            Question.Visibility = Visibility.Visible;
            Reponse_button.Visibility = Visibility.Visible;
            Next_button.Visibility = Visibility.Collapsed;
            System.Diagnostics.Debug.WriteLine("#################################### question brut");
            System.Diagnostics.Debug.WriteLine(question[i].ToString());
            List<string> countword = question[i].Split(' ').ToList();
            if (Marked.Contains(question[i]))
            {
                Icon_Mark.IconFont = FontAwesome.Sharp.IconFont.Solid;
                Marked_tgbutton.IsChecked = true;
            }
            else
            {
                Icon_Mark.IconFont = FontAwesome.Sharp.IconFont.Regular;
            }


            if (action == "question")
            {
                send_data(action, miseneformetext(question[i]), "" , url_question[i], "");
            }
            else
            {
                send_data(action, miseneformetext(question[i]), miseneformetext(repnse[i]), url_question[i], url_rep[i]);
            }
        }

        public static string miseneformetext(string text)
        {
            string question = text.Replace("$", "$$").Replace("$$$", "$").Replace("\\/", "/").Replace("<", "\\lt ").Replace(">", "\\gt ").Replace("\"","'");
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


        private async void Reponse_button_Click(object sender, RoutedEventArgs e)
        {
            questionform(i, "resp");
            Reponse_button.Visibility = Visibility.Collapsed;
            Next_button.Visibility = Visibility.Visible;

        }


        //######################################################################### Button pour affichage de prochaine question

        private void Next_button_Click(object sender, RoutedEventArgs e)
        {
            i++;
            string query = "";
            if (i == id.Count)
            {
                i = 0;
                Question.Visibility = Visibility.Collapsed;
                Endquizz.Visibility = Visibility.Visible;
                try
                {
                    using (SQLiteConnection c = new SQLiteConnection(conSource))
                    {
                        c.Open();
                        
                        query = "UPDATE " + App.Current.Properties["matier"].ToString() + " SET Ended='1' WHERE name = \"" + App.Current.Properties["nameindex"].ToString() + "\"";
                        System.Diagnostics.Debug.WriteLine(query);
                        using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                        {
                            cmd.ExecuteNonQuery();
                        }
                    }
                }
                catch
                {
                    System.Diagnostics.Debug.WriteLine("Error occured while loging the data");
                }
            }
            else
            {
                questionform(i,"question");
                Marked_tgbutton.IsChecked = false;
            }
        }
        private void Back_btn_Click(object sender, RoutedEventArgs e)
        {
            Selection.Visibility = Visibility.Visible;
            Quizzgrid.Visibility = Visibility.Collapsed;
        }



        private void retrievequizz(string nameindex)
        {
            var connection = new SQLiteConnection(conSource);
            string query = "";
            if (App.Current.Properties["matier"] == "all")
            {
                query = "SELECT id,question,reponse,image_question_url,image_answer_url,difficulty FROM " + nameindex;
                App.Current.Properties["matier"] = nameindex;
            }
            else
            {
                query = "SELECT id,question,reponse,image_question_url,image_answer_url,difficulty  FROM " + App.Current.Properties["matier"].ToString() + " WHERE name = \"" + nameindex + "\"";
            }
            try
            {
                connection.Open();
                var command = new SQLiteCommand(query, connection);
                var reader = command.ExecuteReader();
                Aid.Clear();
                Aquestion.Clear();
                Arepnse.Clear();
                Aurl_question.Clear();
                Aurl_rep.Clear();
                Adifficulty.Clear();
                while (reader.Read())
                {
                    Aid.Add(reader.GetString(0));
                    Aquestion.Add(reader.GetString(1));
                    Arepnse.Add(reader.GetString(2));
                    Aurl_question.Add(reader.GetString(3));
                    Aurl_rep.Add(reader.GetString(4));
                    Adifficulty.Add(reader.GetString(5));
                }
            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.ToString());
                System.Diagnostics.Debug.WriteLine(ex.ToString());
            }
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

        private void shuffle()
        {
            id.Clear();
            question.Clear();
            repnse.Clear();
            url_question.Clear();
            url_rep.Clear();
            difficulty.Clear();
            var random = new Random();
            var indices = new List<int>();
            for (int i = 0 ; i < Aid.Count ; i++)
            {
                indices.Add(i);
            }
            for (int i = indices.Count - 1; i > 0; i--)
            { 
                int j = random.Next(i+1);
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
                id.Add(Aid[i]);
                question.Add(Aquestion[i]);
                repnse.Add(Arepnse[i]);
                url_question.Add(Aurl_question[i]);
                url_rep.Add(Aurl_rep[i]);
                difficulty.Add(Adifficulty[i]);
            }
            System.Diagnostics.Debug.WriteLine("Test3");
        }

        private void ViewResp_Click(object sender, RoutedEventArgs e)
        {
            tbTime.Visibility = Visibility.Collapsed;
            Endquizz.Visibility = Visibility.Collapsed;
            allresp.Visibility = Visibility.Visible;
            toolbar.Width = 240;
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) +  "\\..\\..\\..\\HTMl\\Resp" + App.Current.Properties["nameindex"].ToString().Replace(" ","").Replace("è","edb").Replace("ô","o").Replace("é","e").Replace(":","").Replace(".", "") + ".html";
            urif = urif.Replace("\\", "/");
            System.Diagnostics.Debug.WriteLine(urif);
            System.Uri uri1 = new System.Uri(urif);
            if (File.Exists(urif))
            {
                System.Diagnostics.Debug.WriteLine("Il existe");
                webviewall.Source = uri1 as System.Uri;
                System.Diagnostics.Debug.WriteLine("Source webview : ", webviewall.Source);
            }
            else
            {
                Allresp();
                webviewall.Source = uri1 as System.Uri;
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
            marked_list();
            stopwatchlogic();
            retrievequizz(App.Current.Properties["nameindex"].ToString());
            shuffle();
            questionform(i,"question");
            toolbar.Width = 240;
            Quizzgrid.Visibility = Visibility.Collapsed;
            Endquizz.Visibility = Visibility.Collapsed;
            tbTime.Visibility = Visibility.Collapsed;
        }

        private void Allresp()
        {
            string start = "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\r\n   <style>\r\n  img{\r\n  max-width: 60%;\r\n  max-height: 60%;\r\n  max-height: 7cm;\r\n  margin-top: 0.4cm;\r\n  border-radius: 3%;\r\n} .card {\r\n    margin-top: 0.2cm;\r\n     margin-left: 0.2cm;  \r\n box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);\r\n  transition: 0.3s;\r\n    background-color: #" + App.Current.Properties["html_back_rep"] + ";\r\n   width: 40%;\r\n  border-radius: 5px;\r\n  display: inline-block;\r\n  max-width: 13cm;\r\n}\r\n\r p {\r\n    color: " + App.Current.Properties["html_text"] + ";\r\n    padding: 0.2cm;\r\n  }\r\n   \n.card:hover {\r\n  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);\r\n}\r\n\r\n\r\n.container {\r\n  padding: 2px 16px;\r\n}" + "body {\r\n    color: #" + App.Current.Properties["html_back_rep"] + ";\r\n    background-color: #" + App.Current.Properties["html_back"] + ";\r\n}\r\n" + " \r\n</style>\r\n</head>\r\n<body> <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js\"> </script> \r\n ";

            for (int i = 0; i < id.Count; i++)
            {
                if (url_question[i] == "" && url_rep[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n    <p>" + miseneformetext(question[i]) + "</p> \r\n <hr>\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                }
                else if (url_question[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n   <p>" + miseneformetext(question[i])  + "</p> \r\n  <hr>\r\n   <img src=\"" + url_rep[i].Replace("\\/", "/")  + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
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
            string path =System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Resp" + App.Current.Properties["nameindex"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":","").Replace(".","") + ".html";
            path = path.Replace("/", "\\");
            System.Diagnostics.Debug.WriteLine(path);
            File.WriteAllText(path, start);
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
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Resp" + App.Current.Properties["nameindex"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":", "").Replace(".", "") + ".html";
            urif = urif.Replace("\\", "/");
            System.Diagnostics.Debug.WriteLine(urif);
            System.Uri uri1 = new System.Uri(urif);
            if (File.Exists(urif))
            {
                System.Diagnostics.Debug.WriteLine("Il existe");
                webviewall.Source = uri1 as System.Uri;
            }
            else
            {
                Allresp();
                webviewall.Source = uri1 as System.Uri;
            }
        }

        private void stopwatchlogic()
        {
            App.Current.Properties["Timer"] += _stopwatch.ElapsedMilliseconds.ToString();
            _stopwatch.Stop();
            _timer.Stop();
            _stopwatch.Reset();
        }

        private void Marquer_Checked(object sender, RoutedEventArgs e)
        {
            
            string query = "";
            Icon_Mark.IconFont = FontAwesome.Sharp.IconFont.Solid;

            try
            {
                using (SQLiteConnection c = new SQLiteConnection(conSource))
                {
                    c.Open();
                    query = "SELECT COUNT(*) FROM Marked WHERE  question = \"" + question[i] + "\" AND Matier = \"" + App.Current.Properties["matier"].ToString() + "\"";
                    System.Diagnostics.Debug.WriteLine(query);
                    using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                    {
                        long count = (long)cmd.ExecuteScalar();
                        System.Diagnostics.Debug.WriteLine(count);

                        if (count == 0)
                        {
                            string mat = "\"" + App.Current.Properties["matier"].ToString() + "\",";
                            string quest = "\"" + question[i].Replace("\\/", "/") + "\",";
                            string rep = "\"" + repnse[i] + "\",";
                            string question_img = "\"" + url_question[i] + "\",";
                            string reponse_img = "\"" + url_rep[i] + "\"";
                            query = "INSERT INTO Marked (Matier,question,reponse,question_img,reponse_img) VALUES (" + mat + quest + rep + question_img + reponse_img + ")";
                            System.Diagnostics.Debug.WriteLine(query);
                            using (SQLiteCommand insertCmd = new SQLiteCommand(query, c))
                            {
                                insertCmd.ExecuteNonQuery();
                            }
                        }
                    }
                }
            }
            catch
            {
                System.Windows.Forms.MessageBox.Show("An error occured while saving your quizz");
            }
        }

        private void Marquer_Unchecked(object sender, RoutedEventArgs e)
        {
            Icon_Mark.IconFont = FontAwesome.Sharp.IconFont.Regular;
            using (SQLiteConnection c = new SQLiteConnection(conSource))
            {
                c.Open();
                string query = "UPDATE " + App.Current.Properties["matier"].ToString() + " SET Marked = 0 where question = \"" + question[i] + "\" AND name = \"" + App.Current.Properties["nameindex"] + "\"";
                System.Diagnostics.Debug.WriteLine(query);
                using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                {
                    cmd.ExecuteNonQuery();
                }
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
            try
            {
                connection.Open();
                string query = "SELECT name FROM " + App.Current.Properties["matier"].ToString() + " ORDER BY name";
                var command = new SQLiteCommand(query, connection);
                var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    ////Testbox.Items.Add(reader.GetString(0));
                    string y = reader.GetString(0);
                    if (!Name.Contains(y))
                    {
                        Name.Add(y);
                    }
                }
            }
            catch (Exception ex)
            {
                //Testbox.Items.Add(e.ToString());
            }

            ChargerButton(Name,sender);

            connection.Close();
        }




        private void Resppaper_Click(object sender, RoutedEventArgs e)
        {
            System.Windows.Window win = new Response_paper();
            win.Show();
        }

        private void RadioButton_Checked(object sender, RoutedEventArgs e)
        {
            Updateform(Maths, e);
            clear_label("Maths_label",this);

        }
        private void Physique_Checked(object sender, RoutedEventArgs e)
        {
            Updateform(Physique, e);
            clear_label("Physique_label", this);
        }

        private void Si_Checked(object sender, RoutedEventArgs e)
        {
            Updateform(SI, e);
            clear_label("SI_label", this);
        }

        private void All_Checked(object sender, RoutedEventArgs e)
        {
            Updateform(All, e);
            ButtonContainer.Children.Clear();
            Name.Clear();
            List<string> Matier = ["Mathématiques", "Physique", "SI"];
            ChargerButton(Matier, sender);
            App.Current.Properties["matier"] = "all";
            clear_label("All_label", this);
        }

        private void Français_Checked(object sender, RoutedEventArgs e)
        {
            Updateform(Français, e);
            clear_label("Français_label", this);
        }

        private void Anglais_Checked(object sender, RoutedEventArgs e)
        {
            Updateform(Anglais, e);
            clear_label("Anglais_label", this);
        }

        private void Erreur_Checked(object sender, RoutedEventArgs e)
        {
            Updateform(Erreur, e);
            clear_label("Erreurs_label", this);
        }

        private void clear_label(string aimlab, FrameworkElement root)
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

        private async void send_data(string action, string question, string rep, string quest_url, string rep_url)
        {
            //string jsCode = $"updatequizz('{action}','{question}','{rep}','{quest_url}','{rep_url}')";
            //System.Diagnostics.Debug.WriteLine(jsCode);
            var args = new[] { action, question, rep, quest_url.Replace("\\", "/"), rep_url.Replace("\\", "/") };
            string jsCall = $"updatequizz({JsonSerializer.Serialize(args[0])}, {JsonSerializer.Serialize(args[1])}, {JsonSerializer.Serialize(args[2])}, {JsonSerializer.Serialize(args[3])}, {JsonSerializer.Serialize(args[4])})";
            System.Diagnostics.Debug.WriteLine(jsCall);
            System.Diagnostics.Debug.WriteLine(webviewquizz.Source.ToString());

            try
            {
                await webviewquizz.CoreWebView2.ExecuteScriptAsync(jsCall);
            }
            catch { }
        }
    }
}
 