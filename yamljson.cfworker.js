const yaml = await import("./jsyaml.js");
// manually create jsyaml.js, content copy from below url:
// https://github.com/nodeca/js-yaml/blob/master/dist/js-yaml.mjs

// usage: https://yamljson.xx.workers.dev/yamljson/raw.githubusercontent.com/inko16/sing-box-conf-yaml/main/conf.yaml
// to use inside GFW, you may need a custom domain, or deploy it on pages.dev

export default {
  async fetch(request, env, ctx) { 
    let prefix = "/yamljson/";
    if(request.url.includes(prefix)){
      let url = request.url;
      let yamlurl = url.slice(url.indexOf(prefix)+prefix.length);
      if(!yamlurl.startsWith("http"))
        yamlurl = "https://"+yamlurl;
      let dest = new URL(yamlurl);
      let yamlbody = await fetch(dest).then(r=>r.text());
      let jsondest = yaml.load(yamlbody);
      return Response.json(jsondest);
    }
    return new Response('Hello World!');
  },
};
