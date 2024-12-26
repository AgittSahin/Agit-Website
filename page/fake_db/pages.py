
VISION_DETAIL = """
        <div class="row">
            <div class="col-sm-10 offset-sm-1">
                <hr>
                <div>
                <h2>Vision</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis, architecto. Voluptate, vero magnam. Doloremque voluptates necessitatibus exercitationem soluta maxime laudantium quibusdam consequatur cupiditate, dignissimos, alias et repellendus voluptate, blanditiis eos?</p>
                <p>Quam voluptatibus architecto quas illo quidem aut quibusdam ipsa omnis ducimus accusantium tenetur porro possimus eius illum neque alias impedit id magni distinctio non nostrum unde, recusandae molestias error. Facilis.</p>
                <p>Quos laborum eius a expedita. Nobis provident adipisci odio veniam asperiores quo aspernatur tenetur, ex neque excepturi sit unde deleniti velit, voluptates nesciunt minus iusto itaque, dolorem animi eum ut?</p>
                </div>
                <hr>
                <div>
                <h2>Mission</h2>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Molestiae perferendis, nesciunt fugiat sunt consectetur commodi obcaecati ex officia ratione nobis fugit facilis nemo enim dolore architecto. Perspiciatis voluptas incidunt praesentium!</p>
                <p>Libero accusamus iure possimus asperiores laborum pariatur mollitia omnis! Reprehenderit atque illum nostrum adipisci cum iusto, placeat autem aliquam iste quo expedita dolores ab maxime. Reprehenderit minus est nostrum nisi.</p>
                <p>Explicabo sapiente ea officiis minus voluptatibus fuga excepturi adipisci, placeat id eligendi expedita inventore voluptatem modi eveniet, nobis nemo cumque cupiditate accusantium eos sint fugiat consectetur. Laborum at delectus similique?</p>
                <p>Et quod facilis ipsum expedita itaque, doloribus voluptatem sunt dolorum ratione atque quia ea vitae! Odio minus autem sit quo quaerat obcaecati enim, ducimus optio, ut nulla suscipit, corrupti hic.</p>
                <hr>
            </div>
            </div>
        </div>
        <!-- PROJECTS END -->
"""

ABOUT_DETAIL = """
        <div class="row">
            <div class="col-sm-10 offset-sm-1">
                <hr>
                <div>
                <h2>Vision</h2>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis, architecto. Voluptate, vero magnam. Doloremque voluptates necessitatibus exercitationem soluta maxime laudantium quibusdam consequatur cupiditate, dignissimos, alias et repellendus voluptate, blanditiis eos?</p>
                <p>Quam voluptatibus architecto quas illo quidem aut quibusdam ipsa omnis ducimus accusantium tenetur porro possimus eius illum neque alias impedit id magni distinctio non nostrum unde, recusandae molestias error. Facilis.</p>
                <p>Quos laborum eius a expedita. Nobis provident adipisci odio veniam asperiores quo aspernatur tenetur, ex neque excepturi sit unde deleniti velit, voluptates nesciunt minus iusto itaque, dolorem animi eum ut?</p>
                </div>
                <hr>
                <div class="">
                <h2>Mission</h2>
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Molestiae perferendis, nesciunt fugiat sunt consectetur commodi obcaecati ex officia ratione nobis fugit facilis nemo enim dolore architecto. Perspiciatis voluptas incidunt praesentium!</p>
                <p>Libero accusamus iure possimus asperiores laborum pariatur mollitia omnis! Reprehenderit atque illum nostrum adipisci cum iusto, placeat autem aliquam iste quo expedita dolores ab maxime. Reprehenderit minus est nostrum nisi.</p>
                <p>Explicabo sapiente ea officiis minus voluptatibus fuga excepturi adipisci, placeat id eligendi expedita inventore voluptatem modi eveniet, nobis nemo cumque cupiditate accusantium eos sint fugiat consectetur. Laborum at delectus similique?</p>
                <p>Et quod facilis ipsum expedita itaque, doloribus voluptatem sunt dolorum ratione atque quia ea vitae! Odio minus autem sit quo quaerat obcaecati enim, ducimus optio, ut nulla suscipit, corrupti hic.</p>
                <hr>
            </div>
            </div>
        </div>
"""

CONTACT_DETAIL = """
      <!-- Adress Line -->
        <div class="row mb-5">
          <div class="col-sm-10 offset-sm-1">
                <hr>
                <div>
                <h2>Adress</h2>
                <address>
                    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Dolor aliquam eligendi ipsam tenetur, amet nam qui aspernatur. Laborum, eum quis.</p>
                </address>
                <hr>
                <h2>Contact Us</h2>
                <!-- Adress Line END -->
                <!-- Form -->
                <form class="row g-3">
                    <div class="col-12">
                      <label for="inputEmail4" class="form-label">Your Email</label>
                      <input type="email" class="form-control border border-dark" id="inputEmail4">
                    </div>
                    <div class="col-12">
                      <label for="message" class="form-label">Your Message</label>
                      <textarea name="" class="form-control border border-dark" id="message" cols="124" rows="5"></textarea>
                    </div>
                    <div class="col-md-12">
                      <label for="inputCity" class="form-label">City</label>
                      <input type="text" class="form-control border border-dark" id="inputCity">
                    </div>
                    <div class="col-12">
                      <label for="inputState" class="form-label">How did you find us ?</label>
                      <select id="inputState" class="form-select border border-dark">
                        <option selected>Choose...</option>
                        <option>Social Media</option>
                        <option>Google</option>
                        <option>Adress</option>
                        <option>Referance</option>
                      </select>
                    </div>
                    <div class="col-12">
                      <button type="submit" class="btn btn-primary">Submit</button>
                    </div>
                  </form>
                 <!-- Form End -->
                </div>
            </div>
        </div>
"""
HERO_CONTENT = "lorem ipsum soksum siksum sensum lensum denusi kenoli sidou seide hakli hakdel"

FAKE_DB_PAGES = [
    
    {"url": "contact", "detail": CONTACT_DETAIL, "title":"Contact", "hero_title":"Contact", "hero_content":HERO_CONTENT},
    {"url": "vision", "detail": VISION_DETAIL, "title":"Vision", "hero_title":"Vision & Mission", "hero_content":HERO_CONTENT},
    {"url": "about", "detail": ABOUT_DETAIL, "title":"About", "hero_title":"About Us", "hero_content":HERO_CONTENT},
]