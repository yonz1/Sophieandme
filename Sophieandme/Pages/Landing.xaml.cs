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
using LiveCharts;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Data.SQLite;
using FontAwesome.Sharp;
using System.Reflection;
using System.Text.RegularExpressions;
using System.IO;

namespace Sophieandme.Pages
{
    /// <summary>
    /// Logique d'interaction pour Landing.xaml
    /// </summary>
    public partial class Landing : Page
    {

        List<string> question = new List<string>();
        List<string> reponse = new List<string>();
        List<string> url_question = new List<string>();
        List<string> url_rep = new List<string>();

        string conSource = "Data Source=..\\..\\..\\data_restored.db";
        public Landing()
        {
            InitializeComponent();
            readdb_chart();
            readdb();
            string mat = "all";
            Generatevalue(mat);
            string urif = "file:///" + System.IO.Path.GetDirectoryName(Assembly.GetEntryAssembly().Location) + "\\..\\..\\..\\HTMl\\Marked" + mat + ".html";
            urif = urif.Replace("\\", "/");
            System.Diagnostics.Debug.WriteLine(urif);
            System.Uri uri1 = new System.Uri(urif);
            webviewallval.Source = uri1 as System.Uri;
            webviewallval.Visibility = Visibility.Collapsed;
            Textfront.Content = "Welcome back " + App.Current.Properties["username"];
        }
        private void readdb_chart()
        {
            Values1 = new ChartValues<double> { };
            DataContext = this;
            string conSource = "Data Source=C:\\Users\\Bastien\\source\\repos\\WpfApp2\\WpfApp2\\result2.db";
            var connection = new SQLiteConnection(conSource);
            connection.Open();
            Labels = new[] { "" };
            string query = "select date from result_scan_test_manual2";
            var command = new SQLiteCommand(query, connection);
            var reader = command.ExecuteReader();
            List<string> Date = new List<string>();
            while (reader.Read())
            {
                string date = reader.GetString(0);
                if (Date.Count == 0)
                {
                    Date.Add(date);
                }
                else
                {
                    if (!Date.Contains(date))
                    {
                        Date.Add(date);
                    }
                }
            }

            Labels = Date.ToArray();

            foreach (var item in Date)
            {

                double Yvalue = 0;
                string val = "'" + item + "'";
                query = "SELECT COUNT(date) FROM result_scan_test_manual2 WHERE date=" + val;
                command = new SQLiteCommand(query, connection);
                reader = command.ExecuteReader();
                reader.Read();
                Yvalue = reader.GetDouble(0);
                Values1.Add(Yvalue);

            }
            /*try
            {
                for (int i = 0; i < Date.Count; i++)
                {
                    MessageBox.Show(System.Convert.ToString(Date));
                    chart_scanned.Series["0"].Points.AddXY(Date[i], i);
                }
            }
            
            
            catch { MessageBox.Show("error"); }*/




        }

        public ChartValues<double> Values1 { get; set; }
        public string[] Labels { get; set; }


        private void readdb()
        {
            string conSource = "Data Source=C:\\Users\\Bastien\\source\\repos\\WpfApp2\\WpfApp2\\result2.db";
            var connection = new SQLiteConnection(conSource);
            connection.Open();
            string query = "Select * from result_scan_test_manual2";
            var command = new SQLiteCommand(query, connection);
            var reader = command.ExecuteReader();
            string rtot = null;
            int inc = 0;
            int val = 0;
            while (reader.Read())
            {
                //listbox_display.Items.Add(reader.FieldCount);
                rtot = null;
                for (int y = 0; y < reader.FieldCount; y++)
                {
                    inc++;
                    string myread = reader.GetString(y);
                    rtot = rtot + myread + "\n";
                    if (inc == 6)
                    {
                        val++;
                        inc = 0;

                    }
                }
                
            }

            query = "Select * from result_scan_all";
            command = new SQLiteCommand(query, connection);
            reader = command.ExecuteReader();
            rtot = null;
            val = 0;
            int i = 0;
            while (reader.Read())
            {
                //listbox_display.Items.Add(reader.FieldCount);
                rtot = null;
                val++;
                if (i != 20)
                {

                }
                else
                {
                    continue;
                }
                i++;

            }
            val = val / 12;
         


            query = "Select * from Action_file_Dash";
            command = new SQLiteCommand(query, connection);
            reader = command.ExecuteReader();
            int numA = 0;
            while (reader.Read())
            {
                numA++;
            }

            connection.Close();
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
            string start = "<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\r\n   <style>\r\n  img{\r\n  max-width: 60%;\r\n  max-height: 60%;\r\n  max-height: 7cm;\r\n  margin-top: 0.4cm;\r\n  border-radius: 3%;\r\n} .card {\r\n    margin-top: 0.2cm;\r\n     margin-left: 0.2cm;  \r\n box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);\r\n  transition: 0.3s;\r\n    background-color: #" + App.Current.Properties["html_back_rep"] + ";\r\n   width: 40%;\r\n  border-radius: 5px;\r\n  display: inline-block;\r\n  max-width: 13cm;\r\n}\r\n\r p {\r\n    color: white;\r\n    padding: 0.2cm;\r\n  }\r\n   \n.card:hover {\r\n  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);\r\n}\r\n\r\n\r\n.container {\r\n  padding: 2px 16px;\r\n}" + "body {\r\n    color: #" + App.Current.Properties["html_back_rep"] + ";\r\n    background-color: #" + App.Current.Properties["html_back"] + ";\r\n}\r\n" + " \r\n</style>\r\n</head>\r\n<body> <script id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js\"> </script> \r\n ";

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
    }
}
