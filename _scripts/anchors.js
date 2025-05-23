/*
  creates link next to each heading that links to that section.
*/

{
  const onLoad = () => {
    // redirect to /jp/ if at /
    if (window.location.pathname === "/") {
      window.location.href = "/jp/";
      return;
    }

    // for each heading
    const headings = document.querySelectorAll(
      "h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]"
    );
    for (const heading of headings) {
      // create anchor link
      const link = document.createElement("a");
      link.classList.add("icon", "fa-solid", "fa-link", "anchor");
      link.href = "#" + heading.id;
      link.setAttribute("aria-label", "link to this section");
      heading.append(link);

      // if first heading in the section, move id to parent section
      if (heading.matches("section > :first-child")) {
        heading.parentElement.id = heading.id;
        heading.removeAttribute("id");
      }
    }
  };

  // scroll to target of url hash
  const scrollToTarget = () => {
    const id = window.location.hash.replace("#", "");
    const target = document.getElementById(id);

    if (!target) return;
    const offset = document.querySelector("header").clientHeight || 0;
    window.scrollTo({
      top: target.getBoundingClientRect().top + window.scrollY - offset,
      behavior: "smooth",
    });
  };

  // after page loads
  window.addEventListener("load", onLoad);
  window.addEventListener("load", scrollToTarget);
  window.addEventListener("tagsfetched", scrollToTarget);

  // when hash nav happens
  window.addEventListener("hashchange", scrollToTarget);

  // change header to sticky if scrolled past 0.25 of the page and not data-big-header
  // let dataBigTimeout;
  // window.addEventListener("scroll", () => {
  //   const header = document.querySelector("header");
  //   if (!header) return;
    
  //   const scrollY = window.scrollY;
  //   // if at root
  //   clearTimeout(dataBigTimeout);
  //   dataBigTimeout = setTimeout(() => {
  //     if (window.location.pathname.replaceAll(/\/(en|jp)/g, "") === "/") {
  //       const is_big = header.hasAttribute("data-big");
        
  //       if (scrollY > 200 && !is_big) {
  //         header.classList.add("sticky");
  //       } else {
  //         header.classList.remove("sticky");
  //       }
  
  //       if (scrollY > 240) {
  //         header.removeAttribute("data-big");
  //         return;
  //       }
  //       if (!is_big && (scrollY < 100)) {
  //         header.setAttribute("data-big", "");
  //         return;
  //       }
  //     }
  //   }, 100);

  //   // header.classList.toggle("sticky", window.scrollY > 100);
  // });
}
