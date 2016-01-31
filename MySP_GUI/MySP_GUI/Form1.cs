using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MySP_GUI
{
    public partial class MySPForm : Form
    {
        //---How to set to same dir?
        //const string PATH = "\"E:\\12th_grade\\project\\MyProject\\MySP.py\""; 
        const string PATH = "\"D:\\MyProject\\MyProject\\MySP.py\"";
        
        const string HOST = "127.0.0.1";
        const int PORT = 5555;
        string param;
        string msg;

        //Thread pyThrd;
        Process py_proc;
        Socket sockListener, pythonSock;

        public MySPForm()
        {
            InitializeComponent();
            label2.Text = System.IO.Directory.GetCurrentDirectory();
            //const string PATH = 
        }
        
        /*
        private void MyTabControl_Selecting(object sender, TabControlCancelEventArgs e)
        {
            if (e.TabPage == PrivateTab)
                e.Cancel = true;
        }*/

        private void MyRadioButton_CheckedChanged(object sender, EventArgs e)
        {
            LoginButton.Enabled = true;
            LoginButton.Cursor = Cursors.Hand;
        }

        private void UserPassRadioButton_CheckedChanged(object sender, EventArgs e)
        {
            LoginButton.Enabled = true;
            LoginButton.Cursor = Cursors.Hand;
        }

        private void OtherRadioButton_CheckedChanged(object sender, EventArgs e)
        {
            LoginButton.Enabled = true;
            LoginButton.Cursor = Cursors.Hand;
        }

        private void SetInvisible()
        {
            InfoLabel.Visible = false;
            MyRadioButton.Visible = false;
            UserPassRadioButton.Visible = false;
            OtherRadioButton.Visible = false;
            LoginButton.Visible = false;
        }

        private void LoginButton_Click(object sender, EventArgs e)
        {
            SetInvisible();
            if (MyRadioButton.Checked == true)
                param = "MyMainServer";
            else if (UserPassRadioButton.Checked == true)
                param = "UserPassword";
            else
                param = "Other";

            Cursor = Cursors.WaitCursor;
            RunPython();
            Cursor = Cursors.Default;
        }

        private void RunPython()
        {
            py_proc = new Process();
            py_proc.StartInfo.FileName = @"C:\Python27\python.exe";
            py_proc.StartInfo.Arguments = PATH;
            py_proc.StartInfo.UseShellExecute = false;
            py_proc.StartInfo.RedirectStandardOutput = true;
            py_proc.StartInfo.CreateNoWindow = true;
            py_proc.Start();

            sockListener = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            sockListener.Bind(new IPEndPoint(IPAddress.Loopback, PORT));
            sockListener.Listen(1);
            pythonSock = sockListener.Accept();

            if (HandleSocket(pythonSock))
            {
                //MyTabControl.TabPages.Add("My Info");
                //MyTabControl.TabPages
                DisplayUserInfo(msg);
            }
        }

        private bool HandleSocket(Socket clientSock)
        {
            int recv;
            byte[] byData;
            byte[] buf;

            byData = Encoding.ASCII.GetBytes(param);
            pythonSock.Send(byData);
            buf = new byte[1024];

            recv = pythonSock.Receive(buf, buf.Length, 0);
            msg = Encoding.ASCII.GetString(buf, 0, recv);
            //TmpTextBox.Text += msg;

            pythonSock.Shutdown(SocketShutdown.Both);
            pythonSock.Close();

            if (msg == "0")
            {
                FailLabel.Visible = true;
                return false;
            }
            SuccessLabel.Visible = true;
            return true;
        }

        private void DisplayUserInfo(string msg)
        {
            string[] info_arr = msg.Split(' ');
            string name = info_arr[0];
            string phone = info_arr[1];
            string color = info_arr[2];

            GreetingLabel.Text += name + "!";
            NameLabel.Text += name;
            PhoneLabel.Text += phone;
            ColorLabel.Text += color;
        }
    }
}
