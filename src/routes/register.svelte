<script>
    import { register  } from '../lib/api'
    import { goto } from '$app/navigation';
    import { stores_first, stores_nickname, stores_TOKEN } from '../lib/stores.js'


    let id=""
    let username=""
    let password = ""
    let passwordCheck=""
    let registerFailed = false
    let errorMsg=''

    function isInputValide(start, end, value) {
      return (start<=value && value<=end)
    }

    async function registerClick() {
      registerFailed = false
      console.log(id.length)
      if(!isInputValide(2,20,id.length)){
        registerFailed = true
        errorMsg = "아이디는 2글자 이상 20글자 이하여야 합니다."
        return;
      }
      else if(!isInputValide(2, 10, username.length)){
        registerFailed = true
        errorMsg = "닉네임은 2글자 이상 10글자 이하여야 합니다."
        return;
      }
      else if(!isInputValide(6,20,password.length)){
        registerFailed = true
        errorMsg = "비밀번호는 6글자 이상 20글자 이하여야 합니다."
        return;
      }
      else if(password != passwordCheck){
        registerFailed = true
        errorMsg = "비밀번호와 비밀번호 확인이 같지 않습니다."
        return;
      }

      try {
        registerFailed = false
        const res = await register(id, username, password)
        stores_TOKEN.update(x => res.token)
        stores_nickname.update(x => res.nickname)
        stores_first.update(x => res.is_first)
        goto(`/first`)
      } catch (e) {
        registerFailed=true
        errorMsg = e.msg
        console.log(e)
      }
    }

</script>

<svelte:head>
  <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Rubik:400,700'>
</svelte:head>

<div class="login-form">
  <h1>회원가입</h1>
  <div class="content">
    <div class="input-field">
        <input type="text" placeholder="아이디(4-20)" autocomplete="nope" bind:value="{id}">
    </div>
    <div class="input-field">
      <input type="text" placeholder="닉네임(2-10)" autocomplete="nope" bind:value="{username}">
    </div>
    <div class="input-field">
        <input type="password" placeholder="비밀번호(6-20)" autocomplete="nope" bind:value="{password}">
    </div>
    <div class="input-field">
        <input type="password" placeholder="비밀번호 확인(6-20)" autocomplete="nope" bind:value="{passwordCheck}">
    </div>

    {#if registerFailed}
      <div class="error">{errorMsg}</div>
    {/if}
    
  </div>
  <div class="action">
    <button on:click="{registerClick}">가입하기</button>
  </div>
</div>

<style>
   * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}


.login-form {
  background: #fff;
  width: 500px;
  margin: 65px auto;
  display: -webkit-box;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
          flex-direction: column;
  border-radius: 4px;
  box-shadow: 0 2px 25px rgba(0, 0, 0, 0.2);
  /* background: #37DBFF; */
  font-family: 'Pretendard', sans-serif;
}
.error{
  color: red;
  display: flex;
}
.login-form h1 {
  padding: 35px 35px 0 35px;
  font-weight: 300;
}
.login-form .content {
  padding: 35px;
  text-align: center;
}
.login-form .input-field {
  padding: 12px 5px;
}
.login-form .input-field input {
  font-size: 16px;
  display: block;
  font-family: 'Rubik', sans-serif;
  width: 100%;
  padding: 10px 1px;
  border: 0;
  border-bottom: 1px solid #747474;
  outline: none;
  -webkit-transition: all .2s;
  transition: all .2s;
}
.login-form .input-field input::-webkit-input-placeholder {
  text-transform: uppercase;
}
.login-form .input-field input::-moz-placeholder {
  text-transform: uppercase;
}
.login-form .input-field input:-ms-input-placeholder {
  text-transform: uppercase;
}
.login-form .input-field input::-ms-input-placeholder {
  text-transform: uppercase;
}
.login-form .input-field input::placeholder {
  text-transform: uppercase;
}
.login-form .input-field input:focus {
  border-color: #222;
}
.login-form a.link {
  text-decoration: none;
  color: #747474;
  letter-spacing: 0.2px;
  text-transform: uppercase;
  display: inline-block;
  margin-top: 20px;
}
.login-form .action {
  display: -webkit-box;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
          flex-direction: row;
}
.login-form .action button {
  width: 100%;
  border: none;
  padding: 18px;
  font-family: 'Rubik', sans-serif;
  cursor: pointer;
  text-transform: uppercase;
  background: #e8e9ec;
  color: #777;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 0;
  letter-spacing: 0.2px;
  outline: 0;
  -webkit-transition: all .3s;
  transition: all .3s;
}
.login-form .action button{
  background: #2d3b55;
  color: #fff;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 4px;
}
.login-form .action button:hover {
  background: #3c4d6d;
}
</style>
