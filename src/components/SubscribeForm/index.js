import React, { useState } from 'react';
import addToMailchimp from 'gatsby-plugin-mailchimp';
import styles from './SubscribeForm.module.scss';

const SubscribeForm = () => {
  // concept from https://thetrevorharmon.com/blog/email-signup-forms-with-gatsby-and-mailchimp
  const [email, setEmail] = useState('');
  const [status, setStatus] = useState(false);

  const handleSubmit = async (event) => {
    try {
      event.preventDefault();
      const result = await addToMailchimp(email);
      console.log(result);
      setStatus(true);
    } catch (error) {
      console.error(error.message);
      setStatus(false);
    }
  };

  const handleEmailChange = (event) => {
    setEmail(event.currentTarget.value);
  };

  return (
    <form onSubmit={handleSubmit} className={styles.EmailListForm}>
      <h2>Subscribe to my mailing list!</h2>
      {status && <p>Successfully subscribed to Proton's mailing list.</p>}
      <div className={styles.Wrapper}>
        <input
          placeholder="Email address"
          name="email"
          type="text"
          onChange={handleEmailChange}
        />
        <button type="submit">Subscribe</button>
      </div>
    </form>
  );
};

export default SubscribeForm;
