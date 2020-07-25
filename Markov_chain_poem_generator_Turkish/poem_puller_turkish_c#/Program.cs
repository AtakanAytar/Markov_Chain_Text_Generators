using System;
using System.Net;
using System.IO;
using System.Text;
using HtmlAgilityPack;

namespace poem_puller
{
    class Program
    {
        static void get_poems(string file_name,string poem_category,int no_of_pages){
           string myfile = @file_name+".txt";


           StreamWriter sw = File.AppendText(myfile);

           
           
           for(int i=1;i<no_of_pages;i++)
        { 
           try{
           string j=i.ToString();
           string link = "https://www.antoloji.com/"+poem_category+"-"+j+"-siiri/";
           Uri url = new Uri(link);
           WebClient client =new WebClient(); 
           client.Encoding = Encoding.UTF8;
           string html = client.DownloadString(url);
           using (StringReader reader = new StringReader(html)) 
            { 
                string line; 
                while ((line = reader.ReadLine()) != null) 
                { 
                    //Console.WriteLine(line);
                    bool b = line.Contains("pd-text");
                    if(b)
                    {
                      while(line.Contains(@"</p>")==false)
                      {
                        line = reader.ReadLine();
                        if(line.Contains("<br>")==false)
                        {
                            sw.WriteLine(line);
                        }

                      }
                    }
                } 
            } 
           }
           catch(Exception e){

               Console.WriteLine("Skipped");
           }
        }
        Console.WriteLine("Done");
        


            
        }
        static void Main(string[] args)
        {
           get_poems("yalnizlik","yalnizlik",1550);
        
        
        
        }
    }
}
