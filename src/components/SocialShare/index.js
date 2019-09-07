import React from 'react';

import Icon from '../Icon';
import { ICONS } from '../../constants';
import styles from './SocialShare.module.scss';


type Props = {
  siteUrl: string,
  slug: string,
  title: string
};

const SocialShare = ({ slug, siteUrl, title }: Props) => {
  const shareUrl = siteUrl + slug;
  const linkProps = { target: '_blank', rel: 'noopener noreferrer' };
  console.log(styles.social_icon)

  return (
    <section>
      <h3 className={styles.socialHeader}>Share this post</h3>
      <ul className={styles.iconGroup}>
        <li className={styles.social_icon}>
          <a
            href={`https://www.facebook.com/sharer/sharer.php?u=${shareUrl}`}
            {...linkProps}
            className={styles.social_icon__facebook}
          >
            <Icon name="facebookIcon" icon={ICONS.FACEBOOK} />
          </a>
        </li>

        <li className={styles.social_icon}>
          <a
            href={`https://twitter.com/share?url=${shareUrl}&text=${title}&via=Bolaji___`}
            {...linkProps}
            className={styles.social_icon__twitter}
          >
            <Icon name="twitterIcon" icon={ICONS.TWITTER} />
          </a>
        </li>

        <li className={styles.social_icon}>
          <a
            href={`https://www.linkedin.com/shareArticle?url=${shareUrl}&title=${title}&via=Bolaji___`}
            {...linkProps}
            className={styles.social_icon__linkedin}
          >
            <Icon name="twitterIcon" icon={ICONS.LINKEDIN} />
          </a>
        </li>
      </ul>
    </section>
  );
};

export default SocialShare;
