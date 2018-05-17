const puppeteer = require('puppeteer');
const fs = require('fs');

let extract_page_index = async (page, url) => {
  await page.goto(url);
  const result = await page.evaluate(() => {
    return {
      annonces: $(".result-title.hdrlnk").map((x, y) => y.href).toArray(),
      next: $("a.button.next")[0].href,
      prev: $("a.button.prev")[0].href
    }
  });
  return result;
}

let extract_annonce = async (page, url) => {
  await page.goto(url);
  const result = await page.evaluate(() => {
    return {
      body: $("#postingbody").text(),
      title: $("#titletextonly").text() 
    }
  });
  result.url = url;
  return result;
}

let wait_for = (t) => {
  return new Promise((resolve, reject) => {
    setTimeout(resolve, t);
  });
}

let extract_full_page = async (page, url) => {
  console.log(url);
  const index_page = await extract_page_index(page, url);
  let res = [];
  for (let i = 0; i < index_page.annonces.length; i++) {
    await wait_for(3000);
    try {
      let annonce = await extract_annonce(page, index_page.annonces[i]); 
      console.log(annonce.title);
      res.push(annonce);
    } catch (e) {
      console.error(e);
    }
  }
  return {content: res, next: index_page.next };
}

let extract_full_collection = async (name, limit, page, url) => {
  res = [];
  for (let i = 0; i < limit; i++) {
    try {
      let extracted = await extract_full_page(page, url);
      res = res.concat(extracted.content);
      fs.writeFileSync(name, JSON.stringify(res));
      url = extracted.next; 
    } catch (e) {
      console.error(e);
    }
  }
  return res;
}

(async () => {
  const browser = await puppeteer.launch({headless: false});
  const page = await browser.newPage();

  let commu = await extract_full_collection("commu.json", 50, page, "https://newyork.craigslist.org/d/community/search/ccc");

  await browser.close();

})();
