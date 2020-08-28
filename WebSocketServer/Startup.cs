using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using System.Net.WebSockets;

namespace WebSocketServer
{
    public class Startup
    {
        
        public void ConfigureServices(IServiceCollection services)
        {

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)

            app.UseWebSockets();

            app.Use(async (context, next) =>
            {
                if (context.WebSockets.IsWebSocketRequest)
                {
                    WebSocket webSocket = await context.WebSockets.AcceptWebSocketAsync();
                    Console.WriteLine("WebSocket Connected");
                }
                else
                {
                    Console.WriteLine("Hello from 2nd Request Delegate - No WebSocket");
                    await next();
                }
            });         

            app.Run(async context => 
                {   
                Console.WriteLine("Hello from 3rd (terminal) Request Delegate");
                await context.Response.WriteAsync("Hello from 3rd (terminal) Request Delegate");
                });
    }

        private static void WriteRequestParam(HttpContext context, Microsoft.AspNetCore.Hosting.IHostingEnvironment env)
        {
            if (env.IsDevelopment())
            {
                Console.WriteLine("Request Method: " + context.Request.Method);
                Console.WriteLine("Request Protocol: " + context.Request.Protocol);

                if (context.Request.Headers != null)
                {
                    Console.WriteLine("Request Headers: ");
                    foreach (var h in context.Request.Headers)
                    {
                        Console.WriteLine("--> " + h.Key + ": " + h.Value);
                    }
                }
            }


        }
    }
        