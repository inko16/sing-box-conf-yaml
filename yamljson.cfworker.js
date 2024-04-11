const yaml = await import("./jsyaml.js");
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
