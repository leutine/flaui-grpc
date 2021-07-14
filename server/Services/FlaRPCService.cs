using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Grpc.Core;
using Microsoft.Extensions.Logging;
using FlaUI.UIA3;
using FlaUI.Core.Conditions;
using FlaUI.Core.AutomationElements;


namespace Server
{
    public class FlaRPCService : FlaRPC.FlaRPCBase
    {
        private readonly ILogger<FlaRPCService> _logger;
        private static UIA3Automation automation;
        private static FlaUI.Core.Application app;
        private static Window window;
        public FlaRPCService(ILogger<FlaRPCService> logger)
        {
            _logger = logger;
            automation = new UIA3Automation();
        }

        public override Task<Application> Launch(Application application, ServerCallContext context)
        {   
            var app_name = application.Name;
            app = FlaUI.Core.Application.Launch(app_name);
            window = app.GetMainWindow(automation);
            return Task.FromResult(new Application {Name = window.Title});
        }

        public override Task<TypeTextObject> TestTypeText(TypeTextObject typeTextObject, ServerCallContext context)
        {
            _logger.LogWarning(new EventId(), new Exception(), $"ID: {typeTextObject.Element}, Text: {typeTextObject.Text}");
            _logger.LogWarning(new EventId(), new Exception(), $"WINDOW: {window}");

            ConditionFactory cf = new ConditionFactory(new UIA3PropertyLibrary());
            var automation_id = cf.ByAutomationId(typeTextObject.Element);
            _logger.LogWarning(new EventId(), new Exception(), $"CF: {automation_id}");

            var tb = window.FindFirstDescendant(automation_id).AsTextBox();
            _logger.LogWarning(new EventId(), new Exception(), $"TEXTBOX: {tb}");

            tb.Enter(typeTextObject.Text);

            return Task.FromResult(typeTextObject);
        }
    }
}
