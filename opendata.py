<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>路口事故查詢</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        input, button { padding: 8px; font-size: 16px; }
        #result { margin-top: 20px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>台中市路口事故查詢</h1>
    <input type="text" id="roadInput" placeholder="請輸入欲查詢的路名">
    <button onclick="searchRoad()">查詢</button>
    <div id="result"></div>

    <script>
        async function searchRoad() {
            const road = document.getElementById('roadInput').value.trim();
            const resultDiv = document.getElementById('result');
            resultDiv.textContent = "查詢中，請稍候...";

            try {
                const response = await fetch("https://datacenter.taichung.gov.tw/swagger/OpenData/1289c779-6efa-4e7c-bac8-aa6cbe84a58c");
                const data = await response.json();
                let result = "";

                data.forEach(item => {
                    if (item["路口名稱"] && item["路口名稱"].includes(road)) {
                        result += `${item["路口名稱"]}：發生${item["總件數"]}件，主因是${item["主要肇因"]}\n\n`;
                    }
                });

                if (result === "") {
                    resultDiv.textContent = "抱歉，查無相關資料！";
                } else {
                    resultDiv.textContent = result;
                }
            } catch (error) {
                console.error(error);
                resultDiv.textContent = "資料載入失敗，請稍後再試！";
            }
        }
    </script>
</body>
</html>
