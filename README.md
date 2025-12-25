# ✈️ UCUS-API-AUTOMATION

Bu proje, dünya genelindeki canlı uçuş verilerini sağlayan **OpenSky Network API** uç noktalarını test etmek için geliştirilmiş, **Python** tabanlı bir API Test Otomasyon framework'üdür. 

Proje, profesyonel QA süreçlerinde kullanılan **Page Object Model (POM)** mimarisinin API testlerine uyarlanmış halini kullanır.

## 🛠️ Kullanılan Teknolojiler

- **Python 3.13+**: Temel programlama dili.
- **PyTest**: Test framework'ü ve senaryo yönetimi.
- **HTTPX**: Modern, hızlı ve asenkron destekli HTTP istemcisi (API istekleri için).
- **Pytest-HTML**: Test sonuçlarını görselleştirmek için HTML raporlama aracı.

## 🏗️ Proje Mimarisi

Framework, kodun tekrar kullanılabilirliğini (reusability) ve kolay bakımını (maintainability) sağlamak için 3 katmanlı olarak kurgulanmıştır:

- **`utils/api_client.py`**: API motoru. Tüm HTTP istekleri (GET, POST vb.) burada merkezi olarak yönetilir.
- **`tests/conftest.py`**: PyTest fixture'larının bulunduğu yer. Test öncesi kurulum (setup) işlemlerini yapar.
- **`tests/test_flights.py`**: Gerçek test senaryolarının (Pozitif ve Negatif) bulunduğu katman.

## 📋 Test Senaryoları

1.  **Pozitif Test (Happy Path):** Canlı uçuş listesinin başarıyla (HTTP 200) çekilmesi ve veri yapısının doğrulanması.
2.  **Negatif Test (Error Handling):** Geçersiz bir endpoint'e istek atıldığında sistemin doğru hata kodunu (HTTP 404) döndüğünün doğrulanması.
3.  **Veri Validasyonu:** Dönen JSON paketindeki zorunlu alanların  kontrolü.

## 🚀 Kurulum ve Çalıştırma

Projenizi yerel ortamda çalıştırmak için şu adımları izleyin:

1.  **Projeyi klonlayın:**
    ```bash
    git clone [https://github.com/kullanici_adiniz/UCUS-API-AUTOMATION.git](https://github.com/Burakk74/UCUS-API-AUTOMATION.git)
    cd UCUS-API-AUTOMATION
    ```

2.  **Sanal ortam oluşturun ve aktif edin:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows için
    ```

3.  **Bağımlılıkları yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Testleri çalıştırın ve rapor oluşturun:**
    ```bash
    pytest --html=rapor.html --self-contained-html
    ```

## 📊 Raporlama
Testler tamamlandığında proje dizininde oluşan `rapor.html` dosyasını herhangi bir tarayıcı ile açarak detaylı test sonuçlarını görebilirsiniz.


EN
# ✈️ FLIGHT-API-AUTOMATION

This project is a **Python-based API Test Automation Framework** developed to test the **OpenSky Network API** endpoints, which provides global live flight data. 

The framework is designed by adapting the **Page Object Model (POM)** architecture to API testing, ensuring scalability and clean code standards.

## 🛠️ Tech Stack

- **Python 3.13+**: Core programming language.
- **PyTest**: Robust testing framework for scenario management.
- **HTTPX**: Modern and fast HTTP client for handling API requests.
- **Pytest-HTML**: Plugin for generating comprehensive HTML test reports.

## 🏗️ Project Architecture

The framework follows a 3-layered structure to promote reusability and maintainability:

- **`utils/api_client.py` (The Engine)**: Centralized management for all HTTP requests (GET, POST, etc.).
- **`tests/conftest.py` (The Setup)**: Contains PyTest fixtures for global test configurations and setup/teardown logic.
- **`tests/test_flights.py` (The Scenarios)**: Contains actual test cases including Positive, Negative, and Data Validation scenarios.

## 📋 Test Scenarios

1.  **Positive Test (Happy Path):** Validating the successful retrieval (HTTP 200) of the live flight list.
2.  **Negative Test (Error Handling):** Verifying that the system correctly returns an error code (HTTP 404) when an invalid endpoint is requested.
3.  **Data Validation:** Ensuring that the JSON response body contains mandatory fields .

## 🚀 Setup and Execution

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your_username/UCUS-API-AUTOMATION.git](https://github.com/Burakk74/UCUS-API-AUTOMATION.git)
    cd UCUS-API-AUTOMATION
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # For Windows:
    .\venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute tests and generate report:**
    ```bash
    pytest --html=report.html --self-contained-html
    ```

## 📊 Reporting
Once the tests are completed, you can view the detailed results by opening the `report.html` file in your prefered web browser.