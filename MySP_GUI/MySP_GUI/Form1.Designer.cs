namespace MySP_GUI
{
    partial class MySPForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.MyTabControl = new System.Windows.Forms.TabControl();
            this.PublicTab = new System.Windows.Forms.TabPage();
            this.FailLabel = new System.Windows.Forms.Label();
            this.SuccessLabel = new System.Windows.Forms.Label();
            this.LoginButton = new System.Windows.Forms.Button();
            this.OtherRadioButton = new System.Windows.Forms.RadioButton();
            this.UserPassRadioButton = new System.Windows.Forms.RadioButton();
            this.MyRadioButton = new System.Windows.Forms.RadioButton();
            this.InfoLabel = new System.Windows.Forms.Label();
            this.WelcomeLabel = new System.Windows.Forms.Label();
            this.PrivateTab = new System.Windows.Forms.TabPage();
            this.ColorLabel = new System.Windows.Forms.Label();
            this.PhoneLabel = new System.Windows.Forms.Label();
            this.NameLabel = new System.Windows.Forms.Label();
            this.GreetingLabel = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.MyTabControl.SuspendLayout();
            this.PublicTab.SuspendLayout();
            this.PrivateTab.SuspendLayout();
            this.SuspendLayout();
            // 
            // MyTabControl
            // 
            this.MyTabControl.Controls.Add(this.PublicTab);
            this.MyTabControl.Controls.Add(this.PrivateTab);
            this.MyTabControl.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.MyTabControl.Location = new System.Drawing.Point(9, 10);
            this.MyTabControl.Margin = new System.Windows.Forms.Padding(2);
            this.MyTabControl.Name = "MyTabControl";
            this.MyTabControl.SelectedIndex = 0;
            this.MyTabControl.Size = new System.Drawing.Size(652, 392);
            this.MyTabControl.TabIndex = 0;
            // 
            // PublicTab
            // 
            this.PublicTab.BackColor = System.Drawing.Color.Snow;
            this.PublicTab.Controls.Add(this.label2);
            this.PublicTab.Controls.Add(this.FailLabel);
            this.PublicTab.Controls.Add(this.SuccessLabel);
            this.PublicTab.Controls.Add(this.LoginButton);
            this.PublicTab.Controls.Add(this.OtherRadioButton);
            this.PublicTab.Controls.Add(this.UserPassRadioButton);
            this.PublicTab.Controls.Add(this.MyRadioButton);
            this.PublicTab.Controls.Add(this.InfoLabel);
            this.PublicTab.Controls.Add(this.WelcomeLabel);
            this.PublicTab.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PublicTab.Location = new System.Drawing.Point(4, 25);
            this.PublicTab.Margin = new System.Windows.Forms.Padding(2);
            this.PublicTab.Name = "PublicTab";
            this.PublicTab.Padding = new System.Windows.Forms.Padding(2);
            this.PublicTab.Size = new System.Drawing.Size(644, 363);
            this.PublicTab.TabIndex = 0;
            this.PublicTab.Text = "Main Page";
            // 
            // FailLabel
            // 
            this.FailLabel.AutoSize = true;
            this.FailLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.FailLabel.Location = new System.Drawing.Point(142, 107);
            this.FailLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.FailLabel.Name = "FailLabel";
            this.FailLabel.Size = new System.Drawing.Size(242, 40);
            this.FailLabel.TabIndex = 8;
            this.FailLabel.Text = "Unable to connect. \r\nPlease try again or sign up here...";
            this.FailLabel.Visible = false;
            // 
            // SuccessLabel
            // 
            this.SuccessLabel.AutoSize = true;
            this.SuccessLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.SuccessLabel.Location = new System.Drawing.Point(142, 107);
            this.SuccessLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.SuccessLabel.Name = "SuccessLabel";
            this.SuccessLabel.Size = new System.Drawing.Size(311, 60);
            this.SuccessLabel.TabIndex = 7;
            this.SuccessLabel.Text = "You are successfully Connected!\r\nNow you can see your personal information\r\nin \"M" +
    "y Info\" tab!";
            this.SuccessLabel.Visible = false;
            // 
            // LoginButton
            // 
            this.LoginButton.Enabled = false;
            this.LoginButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LoginButton.Location = new System.Drawing.Point(268, 290);
            this.LoginButton.Margin = new System.Windows.Forms.Padding(2);
            this.LoginButton.Name = "LoginButton";
            this.LoginButton.Size = new System.Drawing.Size(86, 32);
            this.LoginButton.TabIndex = 6;
            this.LoginButton.Text = "Go";
            this.LoginButton.UseVisualStyleBackColor = true;
            this.LoginButton.Click += new System.EventHandler(this.LoginButton_Click);
            // 
            // OtherRadioButton
            // 
            this.OtherRadioButton.AutoSize = true;
            this.OtherRadioButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.OtherRadioButton.Location = new System.Drawing.Point(146, 249);
            this.OtherRadioButton.Margin = new System.Windows.Forms.Padding(2);
            this.OtherRadioButton.Name = "OtherRadioButton";
            this.OtherRadioButton.Size = new System.Drawing.Size(79, 24);
            this.OtherRadioButton.TabIndex = 5;
            this.OtherRadioButton.TabStop = true;
            this.OtherRadioButton.Text = "Other...";
            this.OtherRadioButton.UseVisualStyleBackColor = true;
            this.OtherRadioButton.CheckedChanged += new System.EventHandler(this.OtherRadioButton_CheckedChanged);
            // 
            // UserPassRadioButton
            // 
            this.UserPassRadioButton.AutoSize = true;
            this.UserPassRadioButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.UserPassRadioButton.Location = new System.Drawing.Point(146, 210);
            this.UserPassRadioButton.Margin = new System.Windows.Forms.Padding(2);
            this.UserPassRadioButton.Name = "UserPassRadioButton";
            this.UserPassRadioButton.Size = new System.Drawing.Size(258, 24);
            this.UserPassRadioButton.TabIndex = 4;
            this.UserPassRadioButton.TabStop = true;
            this.UserPassRadioButton.Text = "Login with username + password";
            this.UserPassRadioButton.UseVisualStyleBackColor = true;
            this.UserPassRadioButton.CheckedChanged += new System.EventHandler(this.UserPassRadioButton_CheckedChanged);
            // 
            // MyRadioButton
            // 
            this.MyRadioButton.AutoSize = true;
            this.MyRadioButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.MyRadioButton.Location = new System.Drawing.Point(146, 171);
            this.MyRadioButton.Margin = new System.Windows.Forms.Padding(2);
            this.MyRadioButton.Name = "MyRadioButton";
            this.MyRadioButton.Size = new System.Drawing.Size(282, 24);
            this.MyRadioButton.TabIndex = 3;
            this.MyRadioButton.TabStop = true;
            this.MyRadioButton.Text = "Login with MyMainServer (Elizabeth)";
            this.MyRadioButton.UseVisualStyleBackColor = true;
            this.MyRadioButton.CheckedChanged += new System.EventHandler(this.MyRadioButton_CheckedChanged);
            // 
            // InfoLabel
            // 
            this.InfoLabel.AutoSize = true;
            this.InfoLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.InfoLabel.Location = new System.Drawing.Point(142, 107);
            this.InfoLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.InfoLabel.Name = "InfoLabel";
            this.InfoLabel.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.InfoLabel.Size = new System.Drawing.Size(272, 40);
            this.InfoLabel.TabIndex = 1;
            this.InfoLabel.Text = "Dear guest, you are not logged in yet.\r\nTo proceed, you need to log in:";
            // 
            // WelcomeLabel
            // 
            this.WelcomeLabel.AutoSize = true;
            this.WelcomeLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.WelcomeLabel.ForeColor = System.Drawing.Color.Crimson;
            this.WelcomeLabel.Location = new System.Drawing.Point(205, 39);
            this.WelcomeLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.WelcomeLabel.Name = "WelcomeLabel";
            this.WelcomeLabel.Size = new System.Drawing.Size(150, 29);
            this.WelcomeLabel.TabIndex = 0;
            this.WelcomeLabel.Text = "WELCOME!";
            // 
            // PrivateTab
            // 
            this.PrivateTab.AccessibleDescription = "";
            this.PrivateTab.BackColor = System.Drawing.Color.Snow;
            this.PrivateTab.Controls.Add(this.ColorLabel);
            this.PrivateTab.Controls.Add(this.PhoneLabel);
            this.PrivateTab.Controls.Add(this.NameLabel);
            this.PrivateTab.Controls.Add(this.GreetingLabel);
            this.PrivateTab.Controls.Add(this.label1);
            this.PrivateTab.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PrivateTab.Location = new System.Drawing.Point(4, 25);
            this.PrivateTab.Margin = new System.Windows.Forms.Padding(2);
            this.PrivateTab.Name = "PrivateTab";
            this.PrivateTab.Padding = new System.Windows.Forms.Padding(2);
            this.PrivateTab.Size = new System.Drawing.Size(644, 363);
            this.PrivateTab.TabIndex = 1;
            this.PrivateTab.Text = "My Info";
            this.PrivateTab.Visible = false;
            // 
            // ColorLabel
            // 
            this.ColorLabel.AutoSize = true;
            this.ColorLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ColorLabel.Location = new System.Drawing.Point(39, 203);
            this.ColorLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.ColorLabel.Name = "ColorLabel";
            this.ColorLabel.Size = new System.Drawing.Size(184, 24);
            this.ColorLabel.TabIndex = 2;
            this.ColorLabel.Text = "Your favorite color is ";
            // 
            // PhoneLabel
            // 
            this.PhoneLabel.AutoSize = true;
            this.PhoneLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PhoneLabel.Location = new System.Drawing.Point(39, 150);
            this.PhoneLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.PhoneLabel.Name = "PhoneLabel";
            this.PhoneLabel.Size = new System.Drawing.Size(147, 24);
            this.PhoneLabel.TabIndex = 1;
            this.PhoneLabel.Text = "Phone number: ";
            // 
            // NameLabel
            // 
            this.NameLabel.AutoSize = true;
            this.NameLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.NameLabel.Location = new System.Drawing.Point(39, 93);
            this.NameLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.NameLabel.Name = "NameLabel";
            this.NameLabel.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.NameLabel.Size = new System.Drawing.Size(126, 24);
            this.NameLabel.TabIndex = 0;
            this.NameLabel.Text = "Your name is ";
            // 
            // GreetingLabel
            // 
            this.GreetingLabel.AutoSize = true;
            this.GreetingLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GreetingLabel.ForeColor = System.Drawing.Color.Crimson;
            this.GreetingLabel.Location = new System.Drawing.Point(204, 37);
            this.GreetingLabel.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.GreetingLabel.Name = "GreetingLabel";
            this.GreetingLabel.Size = new System.Drawing.Size(103, 29);
            this.GreetingLabel.TabIndex = 0;
            this.GreetingLabel.Text = "HELLO ";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(86, 256);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(496, 26);
            this.label1.TabIndex = 0;
            this.label1.Text = "You are now successfully connected to MySP";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(78, 64);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(66, 24);
            this.label2.TabIndex = 9;
            this.label2.Text = "label2";
            // 
            // MySPForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(670, 411);
            this.Controls.Add(this.MyTabControl);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "MySPForm";
            this.Text = "My Service Provider";
            this.MyTabControl.ResumeLayout(false);
            this.PublicTab.ResumeLayout(false);
            this.PublicTab.PerformLayout();
            this.PrivateTab.ResumeLayout(false);
            this.PrivateTab.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl MyTabControl;
        private System.Windows.Forms.TabPage PublicTab;
        private System.Windows.Forms.RadioButton OtherRadioButton;
        private System.Windows.Forms.RadioButton UserPassRadioButton;
        private System.Windows.Forms.RadioButton MyRadioButton;
        private System.Windows.Forms.Label InfoLabel;
        private System.Windows.Forms.Label WelcomeLabel;
        private System.Windows.Forms.TabPage PrivateTab;
        private System.Windows.Forms.Button LoginButton;
        private System.Windows.Forms.Label FailLabel;
        private System.Windows.Forms.Label SuccessLabel;
        private System.Windows.Forms.Label ColorLabel;
        private System.Windows.Forms.Label PhoneLabel;
        private System.Windows.Forms.Label NameLabel;
        private System.Windows.Forms.Label GreetingLabel;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
    }
}

