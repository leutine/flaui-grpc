using System;
using FlaUI.UIA3;
using FlaUI.Core.Conditions;
using FlaUI.Core.AutomationElements;

namespace Client
{
    class Program
    {
        static void Main(string[] args)
        {
            var app_name = "notepad.exe";
            var app = FlaUI.Core.Application.Launch(app_name);
            var automation = new UIA3Automation();
            var auto_id = "15";
            var text = "absolutely random text";

            Window window = app.GetMainWindow(automation);
            Console.WriteLine($"Window: {window}");
            Console.WriteLine($"Window title: {window.Title}");

            ConditionFactory cf = new ConditionFactory(new UIA3PropertyLibrary());
            var automation_id = cf.ByAutomationId(auto_id);
            Console.WriteLine($"CF: {automation_id}");

            var tb = window.FindFirstDescendant(automation_id).AsTextBox();
            Console.WriteLine($"TEXTBOX: {tb}");

            tb.Enter(text);
        }
    }
}
