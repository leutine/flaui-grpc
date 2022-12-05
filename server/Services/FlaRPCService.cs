using System.Threading.Tasks;
using Grpc.Core;
using Microsoft.Extensions.Logging;
using FlaUI.UIA3;
using FlaUI.Core.Conditions;
using FlaUI.Core.AutomationElements;
using FlaUI.Core;
using FlaUI.Core.Capturing;
using Google.Protobuf;
using System.Drawing;

namespace Server
{
    public class FlaRPCService : FlaRPC.FlaRPCBase
    {
        private readonly ILogger<FlaRPCService> _logger;
        private static UIA3Automation automation;
        private static Application application;
        private static Window window;
        private static ConditionFactory cf;

        public FlaRPCService(ILogger<FlaRPCService> logger)
        {
            _logger = logger;
            automation = new UIA3Automation();
            cf = new ConditionFactory(new UIA3PropertyLibrary());
        }

        public override Task<App> Launch(App app, ServerCallContext context)
        {   
            var app_name = app.Name;
            application = Application.Launch(app_name);
            window = application.GetMainWindow(automation);
            return Task.FromResult(new App {Name = window.Title});
        }

        public override Task<TypeRequest> Type(TypeRequest typeRequest, ServerCallContext context)
        {
            _logger.LogInformation($"By: {typeRequest.By}, Text: {typeRequest.Text}");
            // _logger.LogWarning(new EventId(), new Exception(), $"Window: {window}");

            var automation_id = cf.ByAutomationId(typeRequest.By.AutomationId);
            _logger.LogInformation($"CF: {automation_id}");

            var tb = window.FindFirstDescendant(automation_id).AsTextBox();
            _logger.LogInformation($"Texbox: {tb}");

            tb.Text = typeRequest.Text;

            return Task.FromResult(typeRequest);
        }

        public override Task<Empty> Click(By by, ServerCallContext context)
        {
            _logger.LogInformation($"Click: by={by.ToString()}");

            var automation_id = cf.ByAutomationId(by.AutomationId);
            _logger.LogInformation($"CF: {automation_id}");

            AutomationElement element = window.FindFirstDescendant(automation_id);
            element.Click();

            return Task.FromResult(new Empty());
        }

        public override Task<Empty> ClickCoords(Coordinates coordinates, ServerCallContext context)
        {
            _logger.LogInformation($"Click by coordinates: x={coordinates.X}, y={coordinates.Y}");
            return Task.FromResult(new Empty());
        }

        public static byte[] ImageToBytes(Image img)
        {
            ImageConverter converter = new ImageConverter();
            return (byte[])converter.ConvertTo(img, typeof(byte[]));
        }

        public override Task<File> Screenshot(Empty empty, ServerCallContext context)
        {
            byte[] screenshot_bytes = ImageToBytes(Capture.MainScreen().Bitmap);
            ByteString buffer = ByteString.CopyFrom(screenshot_bytes);

            return Task.FromResult(new File {Buffer = buffer});
        }
    }
}
