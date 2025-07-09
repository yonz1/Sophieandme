using CSharpMath.Forms;
using Microsoft.Web.WebView2.Core;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Data.SQLite;
using System.Diagnostics;
using System.Diagnostics.Metrics;
using System.Diagnostics.SymbolStore;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Media.TextFormatting;
using System.Windows.Navigation;
using System.Windows.Shapes;
using static CSharpMath.Rendering.Text.TextAtom;

namespace Sophieandme.Pages
{ 

    public partial class Custom_quizz : Page
    {
    string conSource = "Data Source=..\\..\\..\\data_restored.db";



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

    // ############################################################## Liste pour le choix des quizz
    List<string> all_quiz = new List<string>();
        List<string> noms = new List<string>();
        List<string> Matier = new List<string>();
        int i = 0;

    private Stopwatch _stopwatch;
    private System.Timers.Timer _timer;
    private const string _startTimeDisplay = "00:00";
    ResourceDictionary res = (ResourceDictionary)App.LoadComponent(new Uri("/Sophieandme;component/Style/ButtonStyle.xaml", UriKind.Relative));



        public Custom_quizz()
        {
            Matier = ["Physique", "Mathématiques", "Français", "Anglais", "Erreurs", "SI"];
            InitializeComponent();
        }

        private async void suggestions()
        {
            string query = "SELECT Name FROM Mathématiques UNION SELECT Name FROM SI UNION SELECT Name FROM Physique";
            var connection = new SQLiteConnection(conSource);
            try
            {
                connection.Open();
                var command = new SQLiteCommand(query, connection);
                var reader = command.ExecuteReader();
                while (reader.Read())
                {
                    noms.Add(reader.GetString(0));
                }
                connection.Close();
                foreach (var item in noms)
                {
                    System.Diagnostics.Debug.WriteLine(item);
                }
            }
            catch (Exception ex)
            {
                System.Diagnostics.Debug.WriteLine(ex.ToString());
            }
            string json = JsonSerializer.Serialize(noms); 
            string jsCode = $"window.nom = {json};";
            System.Diagnostics.Debug.WriteLine(jsCode);
            await webviewall.CoreWebView2.ExecuteScriptAsync(jsCode);
        }



        private async void Create_Click_1(object sender, RoutedEventArgs e)
        {
            Quizzcontain.Visibility = Visibility.Collapsed;
            webview_added.Visibility = Visibility.Collapsed;
            webviewall.Visibility = Visibility.Visible;
            Return_panel.Visibility = Visibility.Collapsed;
            await webviewall.EnsureCoreWebView2Async(null);
            webviewall.CoreWebView2.WebMessageReceived += WebView_WebMessageReceived;
            Create_grid.Visibility = Visibility.Visible;
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTML_const\\Custom.html";
            urif = urif.Replace("\\", "/");
            System.Uri uri1 = new System.Uri(urif);
            webviewall.Source = uri1 as System.Uri;
            suggestions();
        }





        private void WebView_WebMessageReceived(object sender, CoreWebView2WebMessageReceivedEventArgs e)
        {
            Quizzcontain.Children.Clear();
            string Tempsource = "Data Source=..\\..\\..\\user_value.db";
            string json = e.WebMessageAsJson;   
            var data = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, object>>(json);
            System.Diagnostics.Debug.WriteLine(data["action"]);


            if (data["action"].ToString() == "save")
            {
                string query = "";
                string matier = "\"" + data["matier"].ToString() + "\"";
                string nom = "\"" + data["name"].ToString() + "\"";
                string question = "\"" + data["question"].ToString() + "\"";
                string quest_im = "\"" + data["img_question"].ToString() + "\"";
                string rep = "\"" + data["rep"].ToString() + "\"";
                string rep_img = "\"" + data["img_rep"].ToString() + "\"";


                try
                {
                using (SQLiteConnection c = new SQLiteConnection(conSource))
                {
                    c.Open();
                    query = "SELECT COUNT(*) FROM " + matier + " WHERE  name = " + nom + " AND question = " + question;
                    System.Diagnostics.Debug.WriteLine(query);
                    using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                    {
                        long count = (long)cmd.ExecuteScalar();
                        System.Diagnostics.Debug.WriteLine(count);

                        if (count == 0)
                        {
                            query = "INSERT INTO " + matier + " (id,difficulty ,name, question , reponse,image_question_url,image_answer_url,Marked) VALUES (100,1," + nom + "," + question + "," + rep + "," + quest_im + "," + rep_img + ",0)";
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
                MessageBox.Show("An error occured while saving your quizz");
            }
            
            try
            {
                using (SQLiteConnection c = new SQLiteConnection(Tempsource))
                {
                    c.Open();
                    query = "SELECT COUNT(*) FROM Date WHERE  name = " + nom;
                    System.Diagnostics.Debug.WriteLine(query);
                    using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                    {
                        long count = (long)cmd.ExecuteScalar();
                        System.Diagnostics.Debug.WriteLine(count);

                        if (count == 0)
                        {
                            query = "INSERT INTO Date (Name,Inserted) VALUES (" + nom + ",\"" + DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss.ffffff") + "\")";
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
                System.Diagnostics.Debug.WriteLine("Error occured while loging the data");
            }


                //using (SQLiteConnection c = new SQLiteConnection(conSource))
                //{
                //    c.Open();
                //    string query = "INSERT INTO " + matier + " (id,difficulty ,name, question , reponse,image_question_url,image_answer_url,Marked) VALUES (100,1," + nom + "," + question + "," + rep + "," + quest_im + "," + rep_img + ",0)";
                //    System.Diagnostics.Debug.WriteLine(query);
                //    using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                //    {
                //        cmd.ExecuteNonQuery();
                //    }
                //}
                //Thread.Sleep(250);
            }


            else if (data["action"].ToString() == "Delete")
            {
                string val = data["id"].ToString().Replace("\\large", "").Replace("\\(", "$").Replace("\\)", "$");

                string query = "DELETE FROM " + App.Current.Properties["matier"].ToString() + " WHERE ID = \"100\" AND name = \"" + App.Current.Properties["nameindex"].ToString() + "\" AND  REPLACE(question, ' ', '') =  REPLACE(\"" + val + "\", ' ', '')";   
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

                query = "DELETE FROM DATE WHERE Name = \"" + App.Current.Properties["nameindex"].ToString() + "\"";
                using (SQLiteConnection c = new SQLiteConnection(Tempsource))
                {
                    c.Open();
                    System.Diagnostics.Debug.WriteLine(query);
                    using (SQLiteCommand cmd = new SQLiteCommand(query, c))
                    {
                        cmd.ExecuteNonQuery();
                    }
                }
            }
        }

        private void custom_but_Click(object sender, RoutedEventArgs e)
        {
            Quizzcontain.Children.Clear();
            Quizzcontain.Visibility = Visibility.Visible;
            Create_grid.Visibility = Visibility.Collapsed;
            ChargerButton1(Matier, 0);
        }


        private void ChargerButton1(List<string> Name, int val)
        {
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

                if (val == 0)
                {
                    btn.Click += Bouton_click1;
                }
                else
                {
                    btn.Click += Bouton_click2;
                }

                

                Quizzcontain.Children.Add(btn);
            }
        }

        private void Bouton_click1(object sender, RoutedEventArgs e)
        {
            System.Windows.Controls.Button boutonCLique = sender as System.Windows.Controls.Button;
            string Mat = boutonCLique?.Tag as string;
            App.Current.Properties["matier"] = Mat;
            Updateform(sender,e);
            Quizzcontain.Visibility = Visibility.Visible;
            Return_panel.Visibility = Visibility.Collapsed;
            webviewall.Visibility = Visibility.Collapsed;
            webview_added.Visibility = Visibility.Collapsed;
        }

        private async void Bouton_click2(object sender, RoutedEventArgs e)
        {
            System.Windows.Controls.Button boutonCLique = sender as System.Windows.Controls.Button;
            string name = boutonCLique?.Tag as string;
            App.Current.Properties["nameindex"] = name;
            System.Diagnostics.Debug.WriteLine(name);
            retrievequizzData(1);
            Showdata();
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Show" + App.Current.Properties["matier"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":", "").Replace(".", "") + App.Current.Properties["nameindex"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":", "").Replace(".", "") + ".html";
            urif = urif.Replace("\\", "/");
            System.Uri uri1 = new System.Uri(urif);
            webview_added.Source = uri1 as System.Uri;
            Quizzcontain.Visibility = Visibility.Collapsed;
            Return_panel.Visibility = Visibility.Visible;
            webviewall.Visibility = Visibility.Collapsed;
            webview_added.Visibility = Visibility.Visible;
            await webview_added.EnsureCoreWebView2Async(null);
            webview_added.CoreWebView2.WebMessageReceived += WebView_WebMessageReceived;
        }


        //##################################################################################### Fonction pour la logique de quizz : 
        private void retrievequizzData(int value)
        {
            string query = "";
            var connection = new SQLiteConnection(conSource);
                query = "SELECT id,question,reponse,image_question_url,image_answer_url,difficulty,Marked  FROM " + App.Current.Properties["matier"].ToString() + " WHERE id = \"100\" AND name =\"" + App.Current.Properties["nameindex"].ToString() + "\"";

            try
            {
                connection.Open();
                var command = new SQLiteCommand(query, connection);
                var reader = command.ExecuteReader();
                id.Clear();
                question.Clear();
                repnse.Clear();
                url_question.Clear();
                url_rep.Clear();
                difficulty.Clear();
                Marked.Clear();
                while (reader.Read())
                {
                    id.Add(reader.GetString(0));
                    question.Add(reader.GetString(1));
                    repnse.Add(reader.GetString(2));
                    url_question.Add(reader.GetString(3));
                    url_rep.Add(reader.GetString(4));
                    difficulty.Add(reader.GetString(5));
                    Marked.Add(reader.GetString(6));
                }
            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.ToString());
                System.Diagnostics.Debug.WriteLine(ex.ToString());
            }
        }



        private void Showdata()
        {
            string start = "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\r\n   <style>\r\n  img{\r\n  max-width: 60%;\r\n  max-height: 60%;\r\n  max-height: 7cm;\r\n  margin-top: 0.4cm;\r\n  border-radius: 3%;\r\n} .card {\r\n    margin-top: 0.2cm;\r\n     margin-left: 0.2cm;  \r\n box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);\r\n  transition: 0.3s;\r\n    background-color: #" + App.Current.Properties["html_back_rep"] + ";\r\n   width: 40%;\r\n  border-radius: 5px;\r\n  display: inline-block;\r\n  max-width: 13cm;\r\n}\r\n\r p {\r\n font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;\r\n    color: " + App.Current.Properties["html_text"] + ";\r\n    padding: 0.2cm;\r\n  }\r\n   \n.card:hover {\r\n  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);\r\n}\r\n\r\n\r\n.container {\r\n  padding: 2px 16px;\r\n}" + "body {\r\n    color: #" + App.Current.Properties["html_back_rep"] + ";\r\n    background-color: #" + App.Current.Properties["html_back"] + ";\r\n}\r\n" + " \r\n</style>\r\n</head>\r\n<body> <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js\"> </script> \r\n     <link rel=\"stylesheet\" href=\"../HTML_const/Created.css\"> ";

            for (int i = 0; i < id.Count; i++)
            {
                if (url_question[i] == "" && url_rep[i] == "")
                {
                    // Balisage du boutton 
                    start += " <div class=\"card\">\r\n  <div class=\"container\">\r\n    <button class=\"bin-button\" value=\"" + miseneformetext(question[i]) + "\" onclick=\"get_val(this)\">\r\n  <svg\r\n    class=\"bin-top\"\r\n    viewBox=\"0 0 39 7\"\r\n    fill=\"none\"\r\n    xmlns=\"http://www.w3.org/2000/svg\"\r\n  >\r\n    <line y1=\"5\" x2=\"39\" y2=\"5\" stroke=\"white\" stroke-width=\"4\"></line>\r\n    <line\r\n      x1=\"12\"\r\n      y1=\"1.5\"\r\n      x2=\"26.0357\"\r\n      y2=\"1.5\"\r\n      stroke=\"white\"\r\n      stroke-width=\"3\"\r\n    ></line>\r\n  </svg>\r\n  <svg\r\n    class=\"bin-bottom\"\r\n    viewBox=\"0 0 33 39\"\r\n    fill=\"none\"\r\n    xmlns=\"http://www.w3.org/2000/svg\"\r\n  >\r\n    <mask id=\"path-1-inside-1_8_19\" fill=\"white\">\r\n      <path\r\n        d=\"M0 0H33V35C33 37.2091 31.2091 39 29 39H4C1.79086 39 0 37.2091 0 35V0Z\"\r\n      ></path>\r\n    </mask>\r\n    <path\r\n      d=\"M0 0H33H0ZM37 35C37 39.4183 33.4183 43 29 43H4C-0.418278 43 -4 39.4183 -4 35H4H29H37ZM4 43C-0.418278 43 -4 39.4183 -4 35V0H4V35V43ZM37 0V35C37 39.4183 33.4183 43 29 43V35V0H37Z\"\r\n      fill=\"white\"\r\n      mask=\"url(#path-1-inside-1_8_19)\"\r\n    ></path>\r\n    <path d=\"M12 6L12 29\" stroke=\"white\" stroke-width=\"4\"></path>\r\n    <path d=\"M21 6V29\" stroke=\"white\" stroke-width=\"4\"></path>\r\n  </svg>\r\n</button>\r\n";
                    // Balisage de la carte 
                    start += " <p>" + miseneformetext(question[i]) + "</p> \r\n <hr>\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                }
                else if (url_question[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n    <button class=\"bin-button\" value=\"" + miseneformetext(question[i]) + "\" onclick=\"get_val(this)\">\r\n  <svg\r\n    class=\"bin-top\"\r\n    viewBox=\"0 0 39 7\"\r\n    fill=\"none\"\r\n    xmlns=\"http://www.w3.org/2000/svg\"\r\n  >\r\n    <line y1=\"5\" x2=\"39\" y2=\"5\" stroke=\"white\" stroke-width=\"4\"></line>\r\n    <line\r\n      x1=\"12\"\r\n      y1=\"1.5\"\r\n      x2=\"26.0357\"\r\n      y2=\"1.5\"\r\n      stroke=\"white\"\r\n      stroke-width=\"3\"\r\n    ></line>\r\n  </svg>\r\n  <svg\r\n    class=\"bin-bottom\"\r\n    viewBox=\"0 0 33 39\"\r\n    fill=\"none\"\r\n    xmlns=\"http://www.w3.org/2000/svg\"\r\n  >\r\n    <mask id=\"path-1-inside-1_8_19\" fill=\"white\">\r\n      <path\r\n        d=\"M0 0H33V35C33 37.2091 31.2091 39 29 39H4C1.79086 39 0 37.2091 0 35V0Z\"\r\n      ></path>\r\n    </mask>\r\n    <path\r\n      d=\"M0 0H33H0ZM37 35C37 39.4183 33.4183 43 29 43H4C-0.418278 43 -4 39.4183 -4 35H4H29H37ZM4 43C-0.418278 43 -4 39.4183 -4 35V0H4V35V43ZM37 0V35C37 39.4183 33.4183 43 29 43V35V0H37Z\"\r\n      fill=\"white\"\r\n      mask=\"url(#path-1-inside-1_8_19)\"\r\n    ></path>\r\n    <path d=\"M12 6L12 29\" stroke=\"white\" stroke-width=\"4\"></path>\r\n    <path d=\"M21 6V29\" stroke=\"white\" stroke-width=\"4\"></path>\r\n  </svg>\r\n</button>\r\n";
                    start += " <p>" + miseneformetext(question[i]) + "</p> \r\n  <hr>\r\n   <img src=\"" + url_rep[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                }
                else if (url_rep[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n    <button class=\"bin-button\" value=\"" + miseneformetext(question[i]) + "\" onclick=\"get_val(this)\">\r\n  <svg\r\n    class=\"bin-top\"\r\n    viewBox=\"0 0 39 7\"\r\n    fill=\"none\"\r\n    xmlns=\"http://www.w3.org/2000/svg\"\r\n  >\r\n    <line y1=\"5\" x2=\"39\" y2=\"5\" stroke=\"white\" stroke-width=\"4\"></line>\r\n    <line\r\n      x1=\"12\"\r\n      y1=\"1.5\"\r\n      x2=\"26.0357\"\r\n      y2=\"1.5\"\r\n      stroke=\"white\"\r\n      stroke-width=\"3\"\r\n    ></line>\r\n  </svg>\r\n  <svg\r\n    class=\"bin-bottom\"\r\n    viewBox=\"0 0 33 39\"\r\n    fill=\"none\"\r\n    xmlns=\"http://www.w3.org/2000/svg\"\r\n  >\r\n    <mask id=\"path-1-inside-1_8_19\" fill=\"white\">\r\n      <path\r\n        d=\"M0 0H33V35C33 37.2091 31.2091 39 29 39H4C1.79086 39 0 37.2091 0 35V0Z\"\r\n      ></path>\r\n    </mask>\r\n    <path\r\n      d=\"M0 0H33H0ZM37 35C37 39.4183 33.4183 43 29 43H4C-0.418278 43 -4 39.4183 -4 35H4H29H37ZM4 43C-0.418278 43 -4 39.4183 -4 35V0H4V35V43ZM37 0V35C37 39.4183 33.4183 43 29 43V35V0H37Z\"\r\n      fill=\"white\"\r\n      mask=\"url(#path-1-inside-1_8_19)\"\r\n    ></path>\r\n    <path d=\"M12 6L12 29\" stroke=\"white\" stroke-width=\"4\"></path>\r\n    <path d=\"M21 6V29\" stroke=\"white\" stroke-width=\"4\"></path>\r\n  </svg>\r\n</button>\r\n";
                    start += "  <img src=\"" + url_question[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(question[i]) + "</p> \r\n  <hr>\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                }
                else
                {

                    start += " <div class=\"card\">\r\n  <div class=\"container\">\r\n    <button class=\"bin-button\" value=\"" + miseneformetext(question[i]) + "\" onclick=\"get_val(this)\">\r\n  <svg\r\n    class=\"bin-top\"\r\n    viewBox=\"0 0 39 7\"\r\n    fill=\"none\"\r\n    xmlns=\"http://www.w3.org/2000/svg\"\r\n  >\r\n    <line y1=\"5\" x2=\"39\" y2=\"5\" stroke=\"white\" stroke-width=\"4\"></line>\r\n    <line\r\n      x1=\"12\"\r\n      y1=\"1.5\"\r\n      x2=\"26.0357\"\r\n      y2=\"1.5\"\r\n      stroke=\"white\"\r\n      stroke-width=\"3\"\r\n    ></line>\r\n  </svg>\r\n  <svg\r\n    class=\"bin-bottom\"\r\n    viewBox=\"0 0 33 39\"\r\n    fill=\"none\"\r\n    xmlns=\"http://www.w3.org/2000/svg\"\r\n  >\r\n    <mask id=\"path-1-inside-1_8_19\" fill=\"white\">\r\n      <path\r\n        d=\"M0 0H33V35C33 37.2091 31.2091 39 29 39H4C1.79086 39 0 37.2091 0 35V0Z\"\r\n      ></path>\r\n    </mask>\r\n    <path\r\n      d=\"M0 0H33H0ZM37 35C37 39.4183 33.4183 43 29 43H4C-0.418278 43 -4 39.4183 -4 35H4H29H37ZM4 43C-0.418278 43 -4 39.4183 -4 35V0H4V35V43ZM37 0V35C37 39.4183 33.4183 43 29 43V35V0H37Z\"\r\n      fill=\"white\"\r\n      mask=\"url(#path-1-inside-1_8_19)\"\r\n    ></path>\r\n    <path d=\"M12 6L12 29\" stroke=\"white\" stroke-width=\"4\"></path>\r\n    <path d=\"M21 6V29\" stroke=\"white\" stroke-width=\"4\"></path>\r\n  </svg>\r\n</button>\r\n";
                    start += "<img src=\"" + url_question[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(question[i]) + "</p> \r\n  <hr>\r\n   <img src=\"" + url_rep[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(repnse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                }
            }
            start += " <script src=\"../HTML_const/Delete.js\"></script>\r\n  </body>\r\n</html> \r\n";
            string path = System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Show" + App.Current.Properties["matier"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":", "").Replace(".", "") + App.Current.Properties["nameindex"].ToString().Replace(" ", "").Replace("è", "edb").Replace("ô", "o").Replace("é", "e").Replace(":", "").Replace(".", "") + ".html";
            path = path.Replace("/", "\\");
            System.Diagnostics.Debug.WriteLine(path);
            System.IO.File.WriteAllText(path, start);
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

        private void return_btn_Click(object sender, RoutedEventArgs e)
        {
            Quizzcontain.Children.Clear();
            ChargerButton1(Matier, 0);
            webview_added.Visibility = Visibility.Collapsed;
            Return_panel.Visibility = Visibility.Collapsed;
            Quizzcontain.Visibility = Visibility.Visible;
        }
        private void Updateform(object sender, RoutedEventArgs e)
        {
            System.Windows.Controls.Button boutonCLique = sender as System.Windows.Controls.Button;
            string valeur = boutonCLique?.Tag as string;
            Quizzcontain.Children.Clear();
            Name.Clear();
            App.Current.Properties["matier"] = valeur;
            System.Diagnostics.Debug.Write(valeur);
            string query = "SELECT name FROM " + App.Current.Properties["matier"].ToString() + " WHERE ID = \"100\" ORDER BY name";
            System.Diagnostics.Debug.Write(query);
            var connection = new SQLiteConnection(conSource);
            try
            {
                connection.Open();
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

            ChargerButton1(Name, 1);

            connection.Close();
        }
    }
}
