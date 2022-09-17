"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const run = () => __awaiter(void 0, void 0, void 0, function* () {
    // headless로 크롬 드라이버 실행
    let driver = yield new Builder()
        .forBrowser('chrome')
        .setChromeOptions(new chrome.Options().headless().addArguments('--disable-gpu', 'window-size=1920x1080', 'lang=ko_KR'))
        .build();
    try {
        // 특정 URL 생성
        yield driver.get('https://map.kakao.com/');
        let userAgent = yield driver.executeScript('return navigator.userAgent;');
        console.log('[UserAgent]', userAgent);
        // By.id로 #query Element를 얻어온다.
        let searchInput = yield driver.findElement(By.id('search.keyword.query'));
        // keyword를 선택하고 검색 버튼 사용
        let keyword = '닭발';
        searchInput.sendKeys(keyword, Key.ENTER);
        // css selector로 가져온 element가 위치할때까지 최대 10초간 기다린다.
        yield driver.wait(until.elementLocated(By.id('info.search.place.list')), 10000);
        let resultElements = yield driver.findElements(By.className('placetit'));
        // 검색한 elements 하위의 value를 출력함
        console.log('[resultElements.length]', resultElements.length);
        for (var i = 0; i < resultElements.length; i++) {
            console.log('- ' + (yield resultElements[i].getCssValue()));
        }
    }
    catch (e) {
        console.log(e);
    }
    finally {
        driver.quit();
    }
});
run();
//# sourceMappingURL=server.js.map