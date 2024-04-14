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
      console.log(yamlurl);
      if(!yamlurl.startsWith("http"))
        yamlurl = "https://"+yamlurl;
      let dest = new URL(yamlurl);
      console.log(dest);
      let yamlbody = await fetch(dest).then(r=>r.text());
      // extract singbox{...}
      const regex = /singbox{([^}]*)}/;
      const matches = yamlbody.match(regex);
      console.log(matches);

      let jsondest = yaml.load(yamlbody);

      if (matches) {
        // return json as singbox{...} specified
        let sing_obj = matches[1].replace(/ /g,"").split(',');
        console.log(sing_obj);
        let jsonout = {};
        for(let val of sing_obj.values()){
          jsonout[val] = jsondest[val];
        }
        console.log(jsonout);
        return Response.json(jsonout);
        
      }
      return Response.json(jsondest);
    }
    let str =
`inko:
  - ab: cd
    ef: gh
`;
    const jsond = yaml.load(str);
    console.log(jsond);
    return new Response('Hello World!');
  },
};
