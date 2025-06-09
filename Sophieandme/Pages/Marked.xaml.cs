using FontAwesome.Sharp;
using System;
using System.Collections.Generic;
using System.Data.SQLite;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
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

namespace Sophieandme.Pages
{
    /// <summary>
    /// Logique d'interaction pour Marked.xaml
    /// </summary>
    public partial class Marked : Page
    {

        List<string> question = new List<string>();
        List<string> reponse = new List<string>();
        List<string> url_question = new List<string>();
        List<string> url_rep = new List<string>();

        string conSource = "Data Source=..\\..\\..\\data_restored.db";
        public Marked()
        {
            InitializeComponent();
           

        }
        private void Generatevalue(string mat)
        {
            question.Clear();
            reponse.Clear();
            url_question.Clear();
            url_rep.Clear();
            System.Diagnostics.Debug.WriteLine("Test1");
            Getmarked(mat);
            System.Diagnostics.Debug.WriteLine("Test2");
            GenerateHTML(mat);
            foreach (string question in question)
            {
                System.Diagnostics.Debug.WriteLine(question);
            }
            
        }

        private void Getmarked(string mat)
        {
            var connection = new SQLiteConnection(conSource);
            string valtoreq = "question,reponse,image_question_url, image_answer_url";
            string query = "";
            if (mat == "Physique")
            {
                query = "SELECT " + valtoreq + " from Physique where Marked = 1";
            }
            else if (mat == "SI")
            {
                query = "SELECT " + valtoreq + " FROM SI where Marked = 1";
            }
            else if (mat == "Maths")
            {
                query = "SELECT " + valtoreq + " from Mathématiques where Marked = 1";
            }
            else if (mat == "all")
            {
                query = "SELECT " + valtoreq + " from Physique where Marked = 1 UNION SELECT " + valtoreq + " FROM SI where Marked = 1 UNION SELECT " + valtoreq + " from Mathématiques where Marked = 1";
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
                    question.Add(reader.GetString(0));
                    reponse.Add(reader.GetString(1));
                    url_question.Add(reader.GetString(2));
                    url_rep.Add(reader.GetString(3));
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

        private void GenerateHTML(string mat)
        {
            string start = "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\r\n   <style>\r\n  img{\r\n  max-width: 60%;\r\n  max-height: 60%;\r\n  max-height: 7cm;\r\n  margin-top: 0.4cm;\r\n  border-radius: 3%;\r\n} .card {\r\n    margin-top: 0.2cm;\r\n     margin-left: 0.2cm;  \r\n box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);\r\n  transition: 0.3s;\r\n    background-color: #161717;\r\n   width: 40%;\r\n  border-radius: 5px;\r\n  display: inline-block;\r\n  max-width: 13cm;\r\n}\r\n\r p {\r\n    color: white;\r\n    padding: 0.2cm;\r\n  }\r\n   \n.card:hover {\r\n  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);\r\n}\r\n\r\n\r\n.container {\r\n  padding: 2px 16px;\r\n}" + "body {\r\n    color: #161717;\r\n    background-color: #242424;\r\n}\r\n" + " \r\n</style>\r\n</head>\r\n<body> <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js\"> </script> \r\n ";

            for (int i = 0; i < question.Count; i++)
            {
                if (url_question[i] == "" && url_rep[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n    <p>" + miseneformetext(question[i]) + "</p> \r\n <hr>\r\n    <p>" + miseneformetext(reponse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                }
                else if (url_question[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n   <p>" + miseneformetext(question[i]) + "</p> \r\n  <hr>\r\n   <img src=\"" + url_rep[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(reponse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                }
                else if (url_rep[i] == "")
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n   <img src=\"" + url_question[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(question[i]) + "</p> \r\n  <hr>\r\n    <p>" + miseneformetext(reponse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                }
                else
                {
                    start += "<div class=\"card\">\r\n  <div class=\"container\">\r\n   <img src=\"" + url_question[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(question[i]) + "</p> \r\n  <hr>\r\n   <img src=\"" + url_rep[i].Replace("\\/", "/") + "\" alt=\"Avatar\" style=\"width:100%\">\r\n    <p>" + miseneformetext(reponse[i]) + "</p> \r\n  </div>\r\n</div>\r\n";
                }
            }
            start += "</body>\r\n</html> \r\n";
            string path = System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Marked" + mat + ".html";
            path = path.Replace("/", "\\");
            System.Diagnostics.Debug.WriteLine(path);
            File.WriteAllText(path, start);
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


        private void SIM_Click(object sender, RoutedEventArgs e)
        {
            
            string mat = "SI";
            Generatevalue(mat);
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Marked" + mat + ".html";
            urif = urif.Replace("\\", "/");
            System.Diagnostics.Debug.WriteLine(urif);
            System.Uri uri1 = new System.Uri(urif);
            webviewall.Source = uri1 as System.Uri;
            webviewall.Visibility = Visibility.Visible;
        }

        private void AllM_Click(object sender, RoutedEventArgs e)
        {
            
            string mat = "all";
            Generatevalue(mat);
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Marked" + mat + ".html";
            urif = urif.Replace("\\", "/");
            System.Diagnostics.Debug.WriteLine(urif);
            System.Uri uri1 = new System.Uri(urif);
            webviewall.Source = uri1 as System.Uri;
            webviewall.Visibility = Visibility.Visible;
        }

        private void PhysiqueM_Click(object sender, RoutedEventArgs e)
        {
            
            string mat = "Physique";
            Generatevalue(mat);
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Marked" + mat + ".html";
            urif = urif.Replace("\\", "/");
            System.Diagnostics.Debug.WriteLine(urif);
            System.Uri uri1 = new System.Uri(urif);
            webviewall.Source = uri1 as System.Uri;
            webviewall.Visibility = Visibility.Visible;
        }

        private void MathsM_Click(object sender, RoutedEventArgs e)
        {
            
            string mat = "Maths";
            Generatevalue(mat);
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Marked" + mat + ".html";
            urif = urif.Replace("\\", "/");
            System.Diagnostics.Debug.WriteLine(urif);
            System.Uri uri1 = new System.Uri(urif);
            webviewall.Source = uri1 as System.Uri;
            webviewall.Visibility = Visibility.Visible;
        }

        private void Quizz_Click(object sender, RoutedEventArgs e)
        {
            
        }
    }
}
