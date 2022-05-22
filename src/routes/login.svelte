<script>
    import { login  } from '../lib/api'
    import { goto } from '$app/navigation';
    import { stores_TOKEN, stores_nickname, stores_first } from '../lib/stores.js'

    let username=""
    let password = ""
    let loginFailed = false
    let errorMsg=''
    async function signinClick() {
      try {
        loginFailed = false
        const res = await login(username, password)
        stores_TOKEN.update(x => res.token)
        stores_nickname.update(x => res.nickname)
        stores_first.update(x => res.is_first)
        if(res.is_first){
          goto(`/first`)
        }
        else{
          goto(`/`)
        }
        
      } catch (e) {
        loginFailed=true
        errorMsg = e.msg
        console.log(e)
      }
    }

    function registerClick(){
      goto(`/register`)
    }
    const onKeyPress = e => {
        if (e.charCode === 13) signinClick() // 13 : enterKey
    };
</script>

<svelte:head>
  <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Rubik:400,700'>
</svelte:head>

<div class="container">
  <div class="container-image"></div>
  <div class="login-form">
    <h1>Login</h1>
    <div class="content">
      <div class="input-field">
        <input type="text" placeholder="username" autocomplete="nope" bind:value="{username}">
      </div>
      <div class="input-field">
        <input type="password" on:keypress="{onKeyPress}" placeholder="Password" autocomplete="new-password" bind:value="{password}">
      </div>
      {#if loginFailed}
        <div class="error">{errorMsg}</div>
      {/if}
      
      <div class="error"></div>
    </div>
    <div class="action">
      <button on:click="{registerClick}">Register</button>
      <button on:click="{signinClick}">Sign in</button>
    </div>
  </div>
</div>



<style>

  .container {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 90vh;
    margin-bottom: -5rem;
  }
  .container-image {
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
  }
   * {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}


.login-form {
  z-index: 1;
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
.login-form .action button:hover {
  background: #d8d8d8;
}
.login-form .action button:nth-child(2) {
  background: #2d3b55;
  color: #fff;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 4px;
}
.login-form .action button:nth-child(2):hover {
  background: #3c4d6d;
}
</style>
