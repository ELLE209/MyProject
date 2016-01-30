using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net.Sockets;
using System.Net;

namespace Login_GUI
{
    public partial class MyGUIForm : Form
    {
        Socket my_sock;
        const int PORT = 3333;

        public MyGUIForm()
        {
            InitializeComponent();
            my_sock = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
            my_sock.Connect(new IPEndPoint(IPAddress.Loopback, PORT));
        }

        private void LoginButton_Click(object sender, EventArgs e)
        {
            ErrorLabel.Visible = false;
            if (IsUserInfoOK())
            {
                HandleSocket();
                Exit();
            }
            else
                ErrorLabel.Visible = true;
        }

        private bool IsUserInfoOK()
        {
            bool no_username = string.IsNullOrEmpty(UsernameTextBox.Text);
            bool no_password = string.IsNullOrEmpty(PasswordTextBox.Text);

            if (no_username || no_password)
                return false;
            return true;
        }

        private void HandleSocket()
        {
            string credentials;
            byte[] byData;

            credentials = UsernameTextBox.Text + "#" + PasswordTextBox.Text;
            byData = Encoding.ASCII.GetBytes(credentials);
            my_sock.Send(byData); 
        }

        private void Exit()
        {
            my_sock.Close();
            Application.Exit();
        }
    }
}
