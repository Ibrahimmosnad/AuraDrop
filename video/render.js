// Renders video/index.html to a silent MP4:  node video/render.js [--vertical] [out.mp4]  (needs playwright + ffmpeg)
const {chromium}=require(process.env.PLAYWRIGHT_PATH||'playwright');
const {spawn}=require('child_process');const path=require('path');
const vertical=process.argv.includes('--vertical');
const out=process.argv.find(a=>a.endsWith('.mp4'))||path.join(__dirname,vertical?'silent-9x16.mp4':'silent-16x9.mp4');
(async()=>{
  const b=await chromium.launch();const p=await b.newPage({viewport:vertical?{width:1080,height:1920}:{width:1920,height:1080}});
  await p.goto('file://'+path.join(__dirname,'index.html')+(vertical?'?format=vertical':''));
  await p.evaluate(()=>window.ready);
  const {fps,dur}=await p.evaluate(()=>({fps:window.FPS,dur:window.DURATION}));
  const ff=spawn('ffmpeg',['-y','-f','image2pipe','-framerate',String(fps),'-c:v','mjpeg','-i','-','-an','-c:v','libx264','-preset','slow','-crf','16','-pix_fmt','yuv420p','-movflags','+faststart',out],{stdio:['pipe','inherit','inherit']});
  const n=fps*dur;
  for(let f=0;f<n;f++){
    await p.evaluate(t=>window.renderAt(t),f/fps);
    const buf=await p.screenshot({type:'jpeg',quality:95});
    if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));
  }
  ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close();console.log('wrote',out);
})();
