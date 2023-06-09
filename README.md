<a name="readme-top"></a>

<div align="center">
  <h3 align="center">Text-uniqueization for Python Internship by Maklai</h3>
  <p align="center">
    <a href="https://github.com/MultiMilli/text-uniqueization-maklai"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/MultiMilli/text-uniqueization-maklai/issues">Report Bug</a>
    ·
    <a href="https://github.com/MultiMilli/text-uniqueization-maklai/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

API in Python, where an endpoint is implemented, which accepts as input a syntactic tree of English text and returns its paraphrased versions in JSON format.

The Flask framework and the nltk.tree library were used to solve the problem. Paraphrasing was carried out as follows:
* Finding in the tree all NP that consisting of several NP separated by the tags "," (comma) or "СС" (coordinating conjunction).
* Generation of permutations of daughter NPs with each other. In this case, only the parts with the NNS (Noun plural) tag were rearranged to preserve the meaning of the text. In general, other paraphrasing options can also be applied.

You can view the project by following the link: &#128073;[**CLICK HERE**](https://web-production-5280.up.railway.app/paraphrase?tree=(S%20(NP%20(NP%20(DT%20The)%20(JJ%20charming)%20(NNP%20Gothic)%20(NNP%20Quarter)%20)%20(,%20,)%20(CC%20or)%20(NP%20(NNP%20Barri)%20(NNP%20Gòtic)%20)%20)%20(,%20,)%20(VP%20(VBZ%20has)%20(NP%20(NP%20(JJ%20narrow)%20(JJ%20medieval)%20(NNS%20streets)%20)%20(VP%20(VBN%20filled)%20(PP%20(IN%20with)%20(NP%20(NP%20(JJ%20trendy)%20(NNS%20bars)%20)%20(,%20,)%20(NP%20(NNS%20clubs)%20)%20(CC%20and)%20(NP%20(JJ%20Catalan)%20(NNS%20restaurants)%20)%20)%20)%20)%20)%20)%20))

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To run the project locally, follow these steps.

### Installation

1. First, you should have Python3 installed, you can check this with the following command:
   ```sh
   python3 --version
   ```
   If you haven't done this before, click on the link and follow the simple instructions: [**Python3 Installation & Setup Guide**](https://realpython.com/installing-python/#how-to-install-python-on-macos)
2. After that, you need to go to the directory where you plan to place the project and execute the command:
   ```sh
   git clone https://github.com/MultiMilli/text-uniqueization-maklai.git
   ```
3. Create a virtual environment inside the directory. To do this, use the *<cd>* command to go to the cloned directory and perform the following steps:
   ```sh
   python3 -m venv env
   ```
   ```sh
   source env/bin/activate
   ```
4. To install all necessary dependencies, execute the command::
   ```sh
   pip install -r requirements.txt
   ```
4. To launch the project, use the following command:
   ```sh
   flask --app app run 
   ```
5. After that, copy and paste the following URL into the browser, having previously replaced values of *<localhost>* and *<port>*:
   ```sh
   localhost:<port>/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gotic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS restaurants) ) ) ) ) ) ) )
   ```
   
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/maksym-s-b3903122b/) 
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/hi_makss/)

Project Link: [https://github.com/MultiMilli/text-uniqueization-maklai](https://github.com/MultiMilli/text-uniqueization-maklai)

<p align="right">(<a href="#readme-top">back to top</a>)</p>